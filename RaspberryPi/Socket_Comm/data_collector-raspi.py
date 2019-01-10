from multiprocessing import Process, Manager
import socket
import io
import sys
import os
import struct
import picamera
import serial
from time import sleep, time

ser = serial.Serial('/dev/ttyACM0', 9600)

class Stream(Process):
      def __init__(self, arg_dict, lock):
         super(Stream, self).__init__()
         self.video_socket = socket.socket()
         self.video_socket.connect(('192.168.0.8', 8000))
         self.connection = self.video_socket.makefile('wb')
         self.arg_dict = arg_dict
         self.lock = lock

      def run(self):
         with picamera.PiCamera() as camera:
            camera.resolution = (256, 256)
            camera.framerate = 30
            camera.start_preview()
            sleep(2)
   
            count = 0
            start = time()
            stream = io.BytesIO()
            for foo in camera.capture_continuous(stream, 'jpeg', use_video_port=True):

               self.lock.acquire()
               angle_val = self.arg_dict['angle']
               motor_val = self.arg_dict['motor']
               self.lock.release() 
               # TODO: send angle motor value HERE
               print('1')
               self.connection.write(struct.pack('<L', stream.tell()))
               self.connection.flush()
               stream.seek(0)
               self.connection.write(stream.read())
               count += 1
               if time() - start > 30:
                  break;
               stream.seek(0)
               stream.truncate()
         self.connection.write(struct.pack('<L', 0))
         self.connection.close()



def info(title):
         print(title)
         print('module name:', __name__)
         print('parent process:', os.getppid())
         print('process id', os.getpid())

def f(name):
         info('function f')
         print('hello', name)

if __name__ == '__main__':
         manager = Manager()
         x = manager.dict()
         x['angle'] = 1500
         x['motor'] = 170
         l = manager.Lock()
         stream = Stream(x, l)
         stream.start()
         
         print('\t\t still running after Stream.run()')
         # keyboard listener socket create
         listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         server_address = ('0.0.0.0', 8001)
         print('starting up on {}:{}'.format(*server_address))
         listener_socket.bind(server_address)

         listener_socket.listen(1)

         while True:
               print('waiting for a connection')
               connection, client_address = listener_socket.accept()

               try:
                  print('connection from', client_address)

                  while True:
                     l.acquire()
                     angle_val = x['angle']
                     motor_val = x['motor']
                     data_t = connection.recv(1)
                     real_data = data_t.decode('utf-8')
                     data = str( ord(real_data) )
                     print('received {}'.format(data))
                     if data:
                        # TODO: process data HERE
                        # make serial comm HERE
                        angle = int( angle_val )
                        motor = int( motor_val )
                        if data == '0':
                                # Exit Program
                                print('\t\t[+] Shutdown input detectd.')
                                sys.exit(1)
                        elif data == '1':
                                # Forward
                                motor_val = 180
                        elif data == '2':
                                # Left
                                angle_val -= 10 
                        elif data == '3':
                                # Right
                                angle_val += 10
                        elif data == '4':
                                # Stop
                                motor_val = 0

                        # Left Right Max Min modification
                        if angle_val <= 1000:
                                angle_val = 1000
                        elif angle_val >= 2000:
                                angle_val = 2000

                        #if left == 70 and right == 70:
                                #left
                        print('\t[+] Angle: {}, Motor: {}'.format(angle_val, motor_val) )
                        x['angle'] = angle_val
                        x['motor'] = motor_val
                        ser.write(str.encode( str(angle_val) + '\n' ))
                        ser.write(str.encode( str(motor_val) + '\n' ))
                     else:
                        break
               finally:
                  connection.close()
