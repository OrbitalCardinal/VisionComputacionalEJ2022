# -*- coding: utf-8 -*-
"""
Created on Sun May 22 20:03:39 2022

@author: ldgar
"""

import cv2
import numpy as np

# Se hara la lectura de la imagen
img = cv2.imread('flor.png')
cv2.imshow('Original', img)
cv2.waitKey(0)

# Se convierte a nivel de grises
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gris', gray)
cv2.waitKey(0)

# Después se le aplica la detección de bordes por Canny 
edges = cv2.Canny(gray,50,150,apertureSize = 3)
cv2.imshow('Bordes', edges)
cv2.waitKey(0)
lines = cv2.HoughLines(edges,1,np.pi/180,150,None)

# en ocasiones (sobre todo si no se coloca None) la transformada regresa un valor None y todo falla
if lines is not None:
    # Recorrer los resultados
    for i in range(0, len(lines)):
        # Obtener los valores de rho (distacia)
        rho = lines[i][0][0]
		# y de theta (ángulo)
        theta = lines[i][0][1]
		# guardar el valor del cos(theta)
        a = np.cos(theta)
		# guardar el valor del sen(theta)
        b = np.sin(theta)
		# guardar el valor de r cos(theta)
        x0 = a*rho
		# guardar el valor de r sen(theta), todo se está haciendo de forma paramétrica
        y0 = b*rho
        
		# Ahora todo se recorrerá de -1000 a 1000 pixeles
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        
		# Mostrar los valores hallados
        print("({},{})  ({},{})".format(x1,y1, x2,y2))
		# Generar las líneas para montarlas en la imagen original
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

# Mostrar la imagen original con todas las líneas halladas
cv2.imshow('Asia', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
