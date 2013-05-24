import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
import time
import math
from sys import argv

def getDistance(p1, p2):
      #p son listas de coordenadas, en formato [nodo, x, y, z]
    	#p1 representa al punto inicial    
	x1 = p1[1]	#Solo para darle claridad al codigo, aunque salgan mas lineas
	x2 = p2[1]

	y1 = p1[2]	#Solo para darle claridad al codigo, aunque salgan mas lineas
	y2 = p2[2]
	
	z1 = p1[3]
	z2 = p2[3]

    	c = (((x2 - x1)**2) + ((y2-y1)**2) + ((z2-z1)**2))
	distancia = math.sqrt(c)
	return distancia

def main():

    	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	propx = random.randint(0, 5) #Proporcion de crecimiento en el eje x
	ttl = random.randint(0, 4) # Cuantos nodos puede pasar un paquete antes de ser descartado por la red
	cober = random.randint(0, 5) #Cobertura de rango para cada nodo (todos los nodos tienen la misma cobertura)

	#ax.text2D(0.05, 0.95, "Terreno 3D", transform=ax.transAxes)

	ax.set_xlim3d(0, 10)
	ax.set_ylim3d(0, 10)
	ax.set_zlim3d(0, 10)

	c = 'r'
	m = 'o'

	coords = [] # Guardar las coordenadas de cada uno de los nodos en el plano (formato x, y, z)
	listacoords = [] # Guarda cada una de las coordenadas
	n = int(argv[1])	#Para agregar 5 nodos a la simulacion
	for i in range(n):
		if i == 0:
			coords = []
			xs = random.randint(0, 10)
			ys = random.randint(0, 10)
			zs = random.randint(0, 10)
			coords.append(i)
			coords.append(xs)
			coords.append(ys)
			coords.append(zs)
			ax.scatter(xs, ys, zs, c=c, marker=m)
			ax.text(xs, ys, zs, ("nodo: ", i), color='green')
			listacoords.append(coords)

		elif (i != 0) and (i != (n-1)):
			coords = []
			#xs = random.randint(xs+propx, 10)
			xs = xs + propx			
			ys = random.randint(0, 10)
			zs = random.randint(0, 10)
			coords.append(i)
			coords.append(xs)
			coords.append(ys)
			coords.append(zs)
			ax.scatter(xs, ys, zs, c=c, marker=m)
			ax.text(xs, ys, zs, ("nodo: ", i), color='green')
			listacoords.append(coords)
	  	elif i == (n-1):
			c = 'black'
			coords = []
			#xs = random.randint(0, 10)
			xs = xs + propx			
			ys = random.randint(0, 10)
			zs = random.randint(0, 10)
			coords.append(i)
			coords.append(xs)
			coords.append(ys)
			coords.append(zs)
			ax.scatter(xs, ys, zs, c=c, marker=m)
			ax.text(xs, ys, zs, ("Base"), color='green')
			listacoords.append(coords)
			print "\n", i, " es el ultimo elemento del for"
			print coords
	
	ax.set_xlabel('X Label')
	ax.set_ylabel('Y Label')
	ax.set_zlabel('Z Label')
	print listacoords

	distancias = [] # Coleccionar las distancias entre los nodos	
	for j in range(len(listacoords)):
		if j != (len(listacoords)-1):
			print listacoords[j]
			d = getDistance(listacoords[j], listacoords[j+1])
			distancias.append(d)
		else:
			print "Este es el ultimo nodo, osea nodo = ", j
			print listacoords[j]
			
	print "Distancias entre nodos: ", distancias

	print "\nCobertura = ", cober, "\n"

	for x in range(len(distancias)):
		if cober*2 >= distancias[x]:
			print "Existe comunicacion entre nodo ", x, " y nodo ", x+1
		if cober*2 < distancias[x]:
			print "No existe comunicacion por auscencia de cobertura entre nodo ", x, " y nodo ", x+1 
	#getDistance(listacoords)

	print ">>>\nAhora checando estructura del paquete IP, TTL = ", ttl
	if ttl > (n-1):
		print "!!!! El paquete de datos puede ser entregado a la estacion base..."
	else:
		print "**** El paquete no puede ser entregado a la estacion base porque su TTL no es suficiente..." 
	
	plt.show() #Al final para mostrar el plano

main()
