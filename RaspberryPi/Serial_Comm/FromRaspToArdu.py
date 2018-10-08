import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)

while True :
        #ser.write("Hello World\n".encode())
    ser.write("{data: {status: 'go', speed: 10}}\n".encode())

    #print('Hello World')
    time.sleep(0.5)


