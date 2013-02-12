'''
LABORATORIO 2

Diseniar, implementar, comprobar experimentalmente y
documentar un protocolo (simple) a nivel de aplicacion
Usando sockets UDP, mandando bytes
Multiples clientes, un servidor
Cada quien define que en si es el proposito de su
protocolo
Python, C, Ruby o Java de preferencia

Simulacion de DHCP
'''
import socket
import time
import sys

ip = "127.0.0.1"
puerto = 9999

try:
	miSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print "El socket se ha creado \o/"
		
except socket.error, mensaje: #Por si no se crea el socket
	print "Error al crear socket: " + str(mensaje[0]) + " " + mensaje[1]
	sys.exit() #Cerrar el programa

#union de socket con la ip loopback(local) y el puerto 
try:
	miSocket.bind((ip, puerto))
except socket.error, mens: #Por si hay error en la union
	print "Union fallada. Codigo de error:" + str(mens[0]) + " " + mens[1]
	sys.exit() #Cerrar el programa
print "La union se ha completado..."

#Lo siguiente es para recibir peticiones de los clientes y enviarles ip a cada uno

#Direcciones de clase C (Comunmnete las que entrega Telmex)
estatico = "192.168.1."
ultimoOcteto = 250

while True:

	#Recibir mensaje del cliente con parametros (mensaje, ip)
	informacion = miSocket.recvfrom(1024)
	informacion1 = informacion[0]
	informacion2 = informacion[1]

	if not informacion: #Por si no le llega info al servidor
		break

	if ultimoOcteto < 255: #Para enviar direcciones ip que esten dentro del rango, osea menos de 255(que es la direccion de broadcast, en caso de mascara /24)
		direccionEnString = str(ultimoOcteto)	
		enviar = estatico + direccionEnString
		miSocket.sendto(enviar, informacion2)
		print "Envie este mensaje: ", enviar
		ultimoOcteto = ultimoOcteto + 1
	else:
		MensajeAlerta = "Ya no es posible mandar mas direcciones, el pool esta lleno"
		miSocket.sendto(MensajeAlerta, informacion2) #Enviar al cliente que envio su IP request un mensaje que ya no hay IP disponibles
	
	

miSocket.close()
