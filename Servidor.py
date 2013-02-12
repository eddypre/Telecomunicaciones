'''  
LABORATORIO 2

Diseniar, implementar, comprobar experimentalmente y
documentar un protocolo (simple) a nivel de aplicacion
Usando sockets UDP, mandando bytes
Multiples clientes, un servidor
Cada quien define que en si es el proposito de su
protocolo
Python, C, Ruby o Java de preferencia
'''

import socket
import time
#time.sleep(3)

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "bla"
 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
 
while True:
	data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	print "received message:", data
	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
