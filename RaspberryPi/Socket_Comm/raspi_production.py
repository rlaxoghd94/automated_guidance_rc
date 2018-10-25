import socket
import io
import sys
import os
import struct
import picamera
import serial
from time import sleep, time

motor_data

def initConnection():
        sock = socket.socket()
        sock.connect(('192.168.0.8', 8000))
        connection = sock.makefile('wb')
        return connection

if __name__ == '__main__':
        global motor_data
        motor_data = {'left': 0, 'right': 0}

        connection = initConnection()

        with picamera.PiCamera() as camera:
                camera.resolution = (320, 240)
                camera.framerate = 30
                camera.start_preview() # visible on monitor
                sleep(2)

                count = 0
                start = time()
                stream = io.BytesIO()
                for foo in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
                        # TODO: send motor values to the server HERE
                        connection.write( struct.pack('<L', stream.tell()))
                        connection.flush()
                        stream.seek(0)
                        connection.write(stream.read())
                        if time() - start > 10:
                                break
                        stream.seek(0)
                        stream.truncate()
                connection.write( struct.pack('<L', 0) )
                connection.close()
