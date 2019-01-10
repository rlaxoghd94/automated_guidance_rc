import socket
import io
import sys
import os
import struct
import picamera
import serial
from time import sleep, time
import json

CONST_DELAY_INTERVAL = 0.1

ser = serial.Serial('/dev/ttyACM1', 9600)

def initConnection():
        sock = socket.socket()
        sock.connect(('192.168.0.2', 8000))
        connection = sock.makefile('wb')
        return connection

def causeDelay(tval):
        global CONST_DELAY_INTERVAL
        t = CONST_DELAY_INTERVAL - tval
        if t < 0.1:
                sleep(t)
        else:
                sleep(0.1)
                print('\t\t [Warning]: causeDelay received tval greater than 0.1 ({})'.format(tval))

if __name__ == '__main__':
        #global motor_data
        #motor_data = { 'angle_val': 0, 'motor_val' : 0 }
        sock = socket.socket()
        sock.connect(('192.168.0.2', 8000))
        connection = sock.makefile('wb')
        rconnection = sock.makefile('rb')

        with picamera.PiCamera() as camera:
                camera.resolution = (320, 160)
                camera.rotation = 180
                camera.framerate = 30
#                camera.start_preview() # visible on monitor
                sleep(2)

                count = 0
                start = time()
                stream = io.BytesIO()
                for foo in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
                        # TODO: send motor values to the server HERE
                        connection.write( struct.pack('<i', stream.tell()))
                        connection.flush()
                        
                        stream.seek(0)
                        connection.write(stream.read())
                        
                        # TODO: parse response to json
                        angle = struct.unpack_from('<i', rconnection.read(4))[0]
                        
                        motor = 0
                        if angle > 1750 or angle < 1250:
                                motor = 160
                        else:
                                motor = 170

                        print('\t\tAngle: {} Motor: {}'.format(angle, motor) )
                       # ser.write(str.encode( str(angle) + '\0' ))
                        ser.write( str.encode( str(angle) + str(motor) ))
                        sleep(0.1)
                        # ser.write(str.encode( str(motor) + '\0' ))
                        #ser.write( struct.pack('<i', angle) )
                        #ser.write( struct.pack('<i', motor) )

                        tval = time() - start
                        #causeDelay(tval)
                        sleep(0.1)
                        if tval > 10:
                                break
                        stream.seek(0)
                        stream.truncate()
                        start = time()
                        rconnection.flush()
                connection.write( struct.pack('<i', 0) )
                connection.close()
