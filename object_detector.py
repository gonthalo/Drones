import csv
import sys
from PIL import Image
from time import time
import pylab as pl
import numpy as np
from random import random
import cv2
from matplotlib import pyplot as plt

matriz = []

desviacion = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (-1 , -1), (2, 1), (2, 2), (-2, 2), (-1, 2), (-2, -1)]

def generate(n):
	img = Image.new("RGB", (400, 400), "black")
	for ii in range(n):
		px = 5 + int(random()*390)
		py = 5 + int(random()*390)
		color = tuple([int(random()*255) for kk in range(3)])
		for xx, yy in desviacion:
			if px + xx >=0 and px + xx < 400 and py + yy >=0 and py + yy < 400:
				img.putpixel((px + xx, py + yy), color)
	return img

def get_shades(imag):
	lista = []
	for index in range(3):
		imag2 = Image.new("L", imag.size, 0)
		for ii in range(imag.size[0]):
			for jj in range(imag.size[1]):
				imag2.putpixel((ii, jj), imag.getpixel((ii, jj))[index])
		lista.append(imag2)
	return tuple(lista)

def parseimg(imag):
	return [[imag.getpixel((ii, jj)) for jj in range(imag.size[0])] for ii in range(imag.size[1])];

def get_points(archivo):
	total = []
	imag = Image.open(archivo, "r")
	for index in range(3):
		img = get_shades(imag)[index]
		img.save("auxiliar.png")
		img = cv2.imread("auxiliar.png")
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)	
		corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
		corners = np.int0(corners).tolist()
		total += corners
	imag = cv2.imread(archivo)
	for i in np.array(total):
	    x,y = i.ravel()
	    cv2.circle(imag,(x,y),3,255,-1)
	plt.imshow(imag),plt.show()
	return total

imagen1 = generate(4)
imagen1.save("imagen_dron.png")


print get_points("imagen_dron.png")

print get_points("prado.jpg")

print get_points("monte.jpg")



