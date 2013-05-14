import pygame
from pygame.locals import*
from PIL import Image
from math import *
import sys
import numpy
import time
from Tkinter import *
from PIL import Image, ImageTk
import random
from sys import argv
import Image, ImageTk
import Tkinter
from PIL import Image, ImageDraw,ImageFont
import math

def main():  		
	dibujar()

def origenes():
	imagen = Image.open("white.png")
	x, y = imagen.size

	rx = random.randint(110, 400) 		#Intensidades de senial
	ry = rx

	cx = random.randint(110, x-110) 	#Centros de los transmisores
	cy = random.randint(110, y-110)

	return rx, ry, cx, cy

def transmisor1():
	rx, ry = 250, 250
	cx, cy = 200, 300
	return rx, ry, cx, cy
def transmisor2():
	rx, ry = 180, 180
	cx, cy = 300, 400	
	return rx, ry, cx, cy
def transmisor3():
	rx, ry = 250, 250
	cx, cy = 400, 300	
	return rx, ry, cx, cy
def receptor():
	cx, cy = 305, 340
	return cx, cy

def dibujar():
	#nelipses = int(argv[1])
	
	imagen = Image.open("white.png") #Lienzo en blanco
	fuente = ImageFont.truetype('/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-C.ttf',15)
	x, y = imagen.size
	total = x * y
	pixels1 = imagen.load()
	draw = ImageDraw.Draw(imagen)	
	#Primer transmisor *************************************************************************************
	radiox, radioy, centrox, centroy = transmisor1()

	P1 = []
	P1.append(centrox)
	P1.append(centroy)

	box = (centrox - radiox/2, centroy - radioy/2, centrox + radiox/2, centroy + radioy/2)	
	draw.ellipse(box, fill=None, outline= (255,0,0))
	del draw	
	
	#Segundo transmisor ************************************************************************************
	draw = ImageDraw.Draw(imagen)	
	radiox, radioy, centrox, centroy = transmisor2()

	P2 = []
	P2.append(centrox)
	P2.append(centroy)
	
	box = (centrox - radiox/2, centroy - radioy/2, centrox + radiox/2, centroy + radioy/2)
	draw.ellipse(box, fill=None, outline= (0,255,0))
	del draw

	#Tercer transmisor *************************************************************************************
	draw = ImageDraw.Draw(imagen)	
	radiox, radioy, centrox, centroy = transmisor3()
	
	P3 = []
	P3.append(centrox)
	P3.append(centroy) 	
	
	box = (centrox - radiox/2, centroy - radioy/2, centrox + radiox/2, centroy + radioy/2)
	draw.ellipse(box, fill=None, outline= (0,0,255))
	del draw	

	#receptor *********************************************************************************************
	cx, cy = receptor()
	
	R = []
	R.append(cx)
	R.append(cy)

	draw = ImageDraw.Draw(imagen)	
	draw.text((cx, cy), 'receptor ', fill=(0,0,255), font=fuente) #Para pintar el ID de cada figura
	pixels1[cx, cy] = (0,0,0)
	'''
	for i in range(nelipses):
		draw = ImageDraw.Draw(imagen)	
		radiox, radioy, centrox, centroy = origenes()
		box = (centrox - radiox/2, centroy - radioy/2, centrox + radiox/2, centroy + radioy/2)
		r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)  #Asignando pixeles random	
		draw.ellipse(box, fill=None, outline= (r,g,b))
		del draw
	'''			
	d1 = math.sqrt(((R[0] - P1[0])**2) + ((R[1] - P1[1])**2))
	d2 = math.sqrt(((R[0] - P2[0])**2) + ((R[1] - P2[1])**2))
	d3 = math.sqrt(((R[0] - P3[0])**2) + ((R[1] - P3[1])**2))

	i1 = P1[0]
	i2 = P2[0]
	i3 = P3[0]

	j1 = P1[1]
	j2 = P2[1]
	j3 = P3[1]

	x = ((((d1**2 - d2**2) + (i2**2 - i1**2) + (j2**2 - j1**2)) * (2*j3-2*j2)) - (((d2**2 - d3**2) + (i3**2 - i2**2) + (j3**2 - j2**2)) * (2*j2-2*j1))) / (((2*i2-2*i3)*(2*j2-2*j1))-((2*i1 - 2*i2) * (2*j3-2*j2))) 
	
	y = ((d1**2 - d2**2) + (i2**2 - i1**2) + (j2**2 - j1**2) + (x*(2*i1-2*i2))) / (2*j2 - 2*j1)

	newx = int(x)
	newy = int(y)
	print "Coordenadas del receptor = ", x, y
	print "Coordenadas del receptor filtradas = ", newx, newy 

	#d1, d2, d3 = distancia entre puntos P1,2,3 hasta el objetivo
	#i1, i2, i3 = P1.x, P2.x, P3.x respectivamente
	#j1, j2, j3 = P1.y, P3.y, P3.y respectivamente
	#x = coordenadas del objetivo x 
	#y = coordenadas del objetivo y

	#PARA X
	#{ ( [ (d1^2-d2^2) + (i2^2-i1^2) + (j2^2-j1^2) ] * (2*j3-2*j2) - [ (d2^2-d3^2) + (i3^2-i2^2) + (j3^2-j2^2) ] *(2*j2-2*j1) ) /
        #[ (2*i2-2*i3)(2*j2-2*j1)-(2*i1-2*i2)(2*j3-2*j2 ] }

	#PARA Y
	 #y = [ (d1^2-d2^2) + (i2^2-i1^2) + (j2^2-j1^2) + x*(2*i1-2*i2)] / (2*j2-2*j1)

	imagen.save('out.png')

if __name__ == "__main__":
	main()

	
