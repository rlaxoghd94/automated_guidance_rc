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
      def __init__(self):
         super(Stream, self).__init__()
         self.video_socket = socket.socket()
         self.video_socket.connect(('192.168.0.8', 8000))
         self.connection = self.video_socket.makefile('wb')

      def run(self):
         with picamera.PiCamera() as camera:
            camera.resolution = (256, 256)
            camera.framerate = 30
            camera.start_preview()
            sleep(2)
   
            count = 0
            start = time()
            stream = io.BytesIO()
# camera streaming HERE
            for foo in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
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
         x['left'] = 0
         x['right'] = 0
         #stream = Stream()
         #stream.start()
         #stream.join()
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
                     data_t = connection.recv(1)
                     real_data = data_t.decode('utf-8')
                     data = str( ord(real_data) )
                     print('received {}'.format(data))
                     if data:
                        # TODO: process data HERE
                        # make serial comm HERE
                        left = int( x['left'] )
                        right = int( x['right'] )
                        if data == '0':
                                sys.exit()
                        elif data == '1':
                                left = 135
                                right = 135
                        elif data == '2':
                                left -= 5
                                right -= 5
                        elif data == '3':
                                right -= 5
                        elif data == '4':
                                left -= 5
                        elif data == '6':
                                left += 5 
                        elif data == '7':
                                right += 5
                        elif data == '8':
                                left -= 5
                                right -= 10
                        elif data == '9':
                                left -= 10
                                right -= 5

                        # Left Right Max Min modification
                        if left <= 100:
                                left = 100
                        elif left >= 200:
                                left = 200
                        if right <= 100:
                                right = 100
                        elif right >= 200:
                                right = 200

                        #if left == 70 and right == 70:
                                #left
                        print('\t[+] Left: {}, Right: {}'.format(left, right))
                        x['left'] = left
                        x['right'] = right
                        ser.write(str.encode( str(left) + '\n' ))
                        ser.write(str.encode( str(right) + '\n' ))
                     else:
                        break
               finally:
                  connection.close()
