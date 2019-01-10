from time import sleep
import pygame
from pygame.locals import *
import socket

class RCTest():
	def __init__(self):
		pygame.init()
		pygame.display.set_mode((350,350))
		self.serverIP = '192.168.0.10'
		self.serverPort = 8001
		self.val = 'e'
		self.cnt = 0
		self.send_init = True
		
		#socket
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((self.serverIP, self.serverPort))
		self.steer()
		
	def steer(self):
		while(self.send_init):
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					key_input = pygame.key.get_pressed()

               # complex orders
					if key_input[pygame.K_UP] and key_input[pygame.K_RIGHT]:
						print("Forward Right")
						self.val = chr(6)
				
					elif key_input[pygame.K_UP] and key_input[pygame.K_LEFT]:
						print("Forward Left")
						self.val = chr(7)
					
					elif key_input[pygame.K_DOWN] and key_input[pygame.K_RIGHT]:
						print("Reverse Right")
						self.val = chr(8)
					
					elif key_input[pygame.K_DOWN] and key_input[pygame.K_LEFT]:
						print("Reverse Left")                  
						self.val = chr(9)
               
					# simple orders
					elif key_input[pygame.K_UP]:
						print("Forward")
						self.val = chr(1)
					
					elif key_input[pygame.K_DOWN]:
						print("Reverse")
						self.val = chr(2)
					
					elif key_input[pygame.K_RIGHT]:
						print("Right")
						self.val = chr(3)	
					
					elif key_input[pygame.K_LEFT]:
						print("Left")
						self.val = chr(4)				
	
					# exit
					elif key_input[pygame.K_x] or key_input[pygame.K_q]:
						print("Exit")
						self.send_init = False
						self.val = chr(0)
						self.sock.send(self.val.encode())
						sock.close()
						break
					
					self.sock.send(self.val.encode('utf-8'))
						
				elif event.type == pygame.KEYUP:
					self.val = chr(0)
					#self.sock.send(self.val.encode())

if __name__ == '__main__':
	RCTest();
