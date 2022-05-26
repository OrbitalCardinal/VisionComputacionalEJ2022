from math import*
from sys import argv # Importe para tabajar con argumentos
import numpy as np
import cv2
from matplotlib import pyplot as plt
import colorsys
import pandas as pd
from scipy.stats import entropy
import tkinter 
from PIL import Image, ImageTk, ImageDraw, ImageFont
import math
import random


def readImage(imagen_inicial):
    
    imagen_original = Image.open(imagen_inicial)
    imagen_original = imagen_original.convert('RGB')
    #escala de grises
    #toma el valor maximo del rgb de cada pixel
    
    x, y = imagen_original.size
    imagen_gris = Image.new("RGB", (x,y))
    pixeles = []
    for a in range(y):
        for b in range(x):
            r, g, b = imagen_original.getpixel((b, a))
            rgb = (r, g, b)
            data = (r, g, b)
            pixeles.append(data)
    print(pixeles)

    
    return 



def veredictoFinal(imagen_inicial):
    pix = 0
    imperfeccciones = 0
    imagen_original = Image.open(imagen_inicial)
    imagen_original = imagen_original.convert('RGB')
    #escala de grises
    #toma el valor maximo del rgb de cada pixel
    
    x, y = imagen_original.size
    pixeles = []
    for a in range(y):
        for b in range(x):
            r, g, b = imagen_original.getpixel((b, a))
            
            rgb = (r, g, b)
            print(rgb)
            if(r > 10 or g > 10 or b > 10):
                pix += 1
                if(r > 20 or g > 20 or b > 20):
                    imperfeccciones += 1
    print(imperfeccciones, pix)
    porcentaje = (imperfeccciones/pix) * 100
    if(porcentaje > 90):
        print("La fruta muestra irregularidades, nos ha trolleado la madre naturaleza")

    else: 
         print("La fruta no muestra poca o ninguna irregularidad, ¡bien!")
         
    print("Probabilidad de imperfeccion: ", porcentaje)
    return
    

# Detection de esquinas de la imagen


def esquinas(imagen_original):
    imagen_original = Image.open(imagen_original)

    x, y = imagen_original.size
    prueba = imagen_original.load()
    nueva_imagen = imagen_original.copy()
    prueba_nueva = nueva_imagen.load() 
    minimo = 20

    #x es el ancho
    #y es la altura
    for i in range(x):
        for j in range(y):    
            pix = []
            for q in [-1, 0, 1]:
                for w in [-1, 0, 1]:
                    if 0 <= i+q  < x and 0 <= j+w  < y: 
                        pix.append(prueba[i+q,j+w][1])
            pix.sort()
            mediana= len(pix)/2
            
            if len(pix)%2 == 0:
                med=(pix[round(mediana)]+pix[round(mediana)-1])/2
            else:
                med=pix[round(mediana)]  
            prueba_nueva[i,j] = (round(med),round(med),round(med))
    
    for i in range(x):
       for j in range(y):
           otro= prueba_nueva[i,j][0]-prueba[i,j][0]
           if otro < 0:
               otro = 0
           if otro > 255:
               otro = 255
           if otro > minimo:
               prueba[i,j]= (otro,otro,otro)
           else:
               prueba[i,j]=(0,0,0)
    lista = []

    for i in range(x):
        for j in range(y):
            if imagen_original.getpixel((i,j))!=(0,0,255) and imagen_original.getpixel((i,j))!=(0,0,0):
                lista.append(( imagen_original, (0,0,255)))
                for a in range(-2,3):
                    for b in range(-2,3):
                        if 0 <= i+a  < x and 0 <= j+b  < y:
                            prueba[i+a,j+b] = (0,0,255)
    
    imagen_original.save('output6.png') 
    print("6- Uso de mascaras para el resaltado de la imagen", prueba)
    return imagen_original, lista


def hsl(imagen_inicial):
    
    imagen_original = Image.open(imagen_inicial)
    imagen_original = imagen_original.convert('RGB')
    #escala de grises
    #toma el valor maximo del rgb de cada pixel
    
    x, y = imagen_original.size
    imagen_gris = Image.new("RGB", (x,y))
    pixeles = []
    for a in range(y):
        for b in range(x):
            r, g, b = imagen_original.getpixel((b, a))
            rgb = (r, g, b)
                #normalize
            (r, g, b) = (r / 255, g / 255, b / 255)
    #convert to hsv
            (h, s, v) = colorsys.rgb_to_hsv(r, g, b)
    #expand HSV range
            (h, s, v) = (int(h * 179), int(s * 255), int(v * 255))
            #print('HSV : ', h, s, v)
            (r, g, b) = colorsys.hsv_to_rgb(h, s, v)
            data = (h, s, v)
            pixeles.append(data)
    print("5- En este paso convertimos nuestra imagen resultante de RHB a HSI", pixeles)
    
    imagen_gris.putdata(pixeles)
    imagen_gris.save("output5.png")
    

    #normalize
    #(r, g, b) = (r / 255, g / 255, b / 255)
    #convert to hsv
    #(h, s, v) = colorsys.rgb_to_hsv(r, g, b)
    #expand HSV range
    #(h, s, v) = (int(h * 179), int(s * 255), int(v * 255))
    #print('HSV : ', h, s, v)
    
    return imagen_gris


def gris(imagen_inicial):
    
    imagen_original = Image.open(imagen_inicial)
    imagen_original = imagen_original.convert('RGB')
    #escala de grises
    #toma el valor maximo del rgb de cada pixel
    
    x, y = imagen_original.size
    imagen_gris = Image.new("RGB", (x,y))
    pixeles = []
    for a in range(y):
        for b in range(x):
            r, g, b = imagen_original.getpixel((b, a))
            rgb = (r, g, b)
                #se elige el valor mas grande
            maximo = max(rgb)
            data = (maximo, maximo, maximo)
            pixeles.append(data)
    imagen_gris.putdata(pixeles)
    imagen_gris.save("imagen_gris.png")
    print("Matriz convertida a escala de grises: ", pixeles)
    return imagen_gris

def obtener_matrices(image):
    image = Image.open(image) 
    pixels = image.load()
    ancho,alto = image.size
    matrizr = np.empty((ancho, alto))
    matrizg = np.empty((ancho, alto))
    matrizb = np.empty((ancho, alto))
    for i in range(ancho):
        for j in range(alto):
            a = image.getpixel((i,j))
            #escala = (a[0] + a[1] + a[2])/3	
            #r,g,b = image.getpixel((i,j))
            #escala= (r+g+b)/3
            #pixels[i,j] = (round(escala), round(escala), round(escala))
            matrizr[i,j] = a[0]
            matrizg[i,j] = a[1]
            matrizb[i,j] = a[2]
            
        
    print("2- Aplicamos un filtro para segmentar por color antes de aplicar bordes", matrizr)
    print("2- Aplicamos un filtro para segmentar por color antes de aplicar bordes", matrizg)
    print("2- Aplicamos un filtro para segmentar por color antes de aplicar bordes", matrizb)        
    df = image.save('escala.png')
    return image,matrizr, matrizg, matrizb

def vecindad(i,j,lista,matriz, promedio):
    promedio = 0
    indice  = 0
    for x in lista:
        for y in lista:
            a = i+x
            b = j+y
            try:
                if matriz[a,b] and (x!=a and y!=b):
                    promedio += matriz[a,b]
                    indice +=1            
            except IndexError:
                pass
            try:
                promedio=int(promedio/indice)
                return promedio
            except ZeroDivisionError:
                return 0  

def filtro(image):
    image, matrizr, matrizg, matrizb = obtener_matrices(image)
    pixels = image.load()
    ancho, alto =image.size
    lista = [-1,0,1]
    for i in range(ancho):
        for j in range(alto):
            promedior = vecindad(i,j,lista, matrizr, 35)
            promediog = vecindad(i,j,lista, matrizg, 55)
            promediob = vecindad(i,j,lista, matrizb, 28)
            #if(promedior < 75 and promedior >  15):
            #    if(promediog < 95 and promediog >  15):
            #        if(promediob < 68 and promediob > 18):
            pixels[i,j] = (promedior,promediog,promediob)
            #else:
                #pixels[i,j] = (0,0,0)
                
            
    image.save('PIAVecindarios.png')
    print("Matriz de los vaolores de los filtros: ", pixels)
    return image


    
def contraste(img):
    image1 = Image.open(img)
    pixels = image1.load()
    ancho,alto = image1.size
    minimo = 60 #toma un valor umbral minimo
    for i in range(ancho):
        for j in range(alto):
            #a = pixels[i,j]
            #escala = (a[0] + a[1] + a[2])/3    
            #escala = int(escala)
            #print(escala)
            
            #pixels[i,j] = (escala,escala,escala)
            #print("Si ",pixels[i,j][0] , " es menor que ", minimo)
            if pixels[i,j][0] <= minimo and pixels[i,j][1] <= minimo and pixels[i,j][2] <= minimo:
                p=0

                
    imagen = filtro(img)
    new = 'output1.png'
    image1.save(new)
    print("Matriz de el contraste de la imagen: ", pixels)
    #fin = time()
    #tiempo_t = fin - inicio
    #print "Tiempo que tardo en ejecutarse binzarizar = "+str(tiempo_t)+" segundos"
    return image1

def entropia(imagen_inicial):
    imagen_original = Image.open(imagen_inicial)
    imagen_original = imagen_original.convert('RGB')
    #escala de grises
    #toma el valor maximo del rgb de cada pixel
    
    x, y = imagen_original.size
    imagen_gris = Image.new("RGB", (x,y))
    pixeles = []
    for a in range(y):
        for b in range(x):
            pd_series = pd.Series(a)
            counts = pd_series.value_counts()
            entropya = entropy(counts)
                #se elige el valor mas grande
            data = (int(round(entropya)), int(round(entropya)), int(round(entropya)))
            pixeles.append(data)
    imagen_gris.putdata(pixeles)
    imagen_gris.save("output7.png")
    print("Matriz de la entropia de la imagen: ", pixeles)
    return entropya   


    

def main(file):
    # 1- Adquisicion de la imagen RGB

    
    image = Image.open(file)
    img = cv2.imread(file)
    res = cv2.resize(img, dsize=(480, 480), interpolation=cv2.INTER_CUBIC)
    img1 = cv2.imwrite(file, res)
    plt.imshow(img)
    input("Oprime un boton para continuaar...")
    
    # 1.1 - Obtencion de vecindarios, filtro de clasificacion por colores
    Output1 = contraste(file)
    output1 = cv2.imread('output1.png')
    plt.imshow(output1)
    input("Oprime un boton para continuaar...")
    
    # 2 Detectamos las esquinas de la hoja
    Output2 = gris('output1.png')
    #Output2 = esquina(Output2)
    output2 = cv2.imread('imagen_gris.png')
    gray = cv2.cvtColor(output2,cv2.COLOR_BGR2GRAY)
    plt.imshow(output2)
    input("Oprime un boton para continuaar...")
    
    output3 = cv2.imread('output2.png')
    output3 = cv2.Canny(gray,50,150,apertureSize = 3)
    cv2.imwrite("output3.png", output3)
    output3 = cv2.imread('output3.png')
    print("2- Borde Generado, matriz a continuacion")
    readImage("output3.png")
    plt.imshow(output3)
    input("Oprime un boton para continuaar...")
    
    # 3 - Anulamos el ruido de la imagen resultante
    dst = cv2.fastNlMeansDenoisingColored(output3,None,10,10,7,21)
    output4 = cv2.imwrite("output4.png", dst)
    output4 = cv2.imread('output4.png')
    print("3- Ruido anulado, matriz a continuacion")
    readImage("output4.png")
    plt.imshow(output4)
    input("Oprime un boton para continuaar...")
    
    # 4 - Acortamos la imagen
    img4 = cv2.imread('output4.png')
    res = cv2.resize(img4, dsize=(240, 240), interpolation=cv2.INTER_CUBIC)
    Output41 = cv2.imwrite("output4.1.png", res)
    Output41 = cv2.imread('output4.1.png')
    print("4- Reduccion de imagen, matriz a continuacion")
    readImage("output3.png")
    plt.imshow(Output41)
    input("Oprime un boton para continuaar...")

    
    # 5 - RGB a HSI 
    hsi = hsl("output4.1.png")
    #cv2.imwrite("output5.png", hsi)
    output5 = cv2.imread('output5.png')
    
    # 6 - Generacion de algunas de las pruebas de textura como mascaras para generar un resultado
    esquinas("output4.1.png")
    #entropia("output1.png")
    output6 = cv2.imread('output6.png')
    output7 = cv2.imread('output7.png')
    
    
    # 7 Estadisticas
    veredictoFinal("output5.png") 
    
    
    
    plt.subplot(181),plt.imshow(img)
    plt.subplot(182),plt.imshow(output1)
    plt.subplot(183),plt.imshow(output3)
    plt.subplot(184),plt.imshow(dst)
    plt.subplot(185),plt.imshow(output4)
    plt.subplot(186),plt.imshow(Output41)
    plt.subplot(187),plt.imshow(output5)
    plt.subplot(188),plt.imshow(output6)
    

    
    
#return new


while True:
    #file = input("Esccribe el nombre de la imagen")
    file = "orange_blasco.png"
    try:
        cv2.imread(file)
        main(file)
        break
    except FileNotFoundError:
        print("Imagen no encontrada, revise que este en el mismo directorio: ", FileNotFoundError)


