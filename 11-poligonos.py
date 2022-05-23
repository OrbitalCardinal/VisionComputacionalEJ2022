import cv2
import numpy as np

img = cv2.imread('formas.png')
cv2.imshow('original', img)    
cv2.waitKey(0) 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #convertir en escala de grises
edged = cv2.Canny(gray, 170, 255)            #con esto determina los bordes de los objetos
ret,thresh = cv2.threshold(gray,240,255,cv2.THRESH_BINARY)  
(contours,_) = cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #para encontrar los contornos de una imagen
def detectShape(c): #funcion principal para detectar el numero de lados 
       shape = 'unknown'
       
       peri=cv2.arcLength(cnt,True) 
       vertices = cv2.approxPolyDP(cnt, 0.02 * peri, True)
       
       sides = len(vertices)
       lados = str(sides)
       print(lados)
       if (sides == 3): 
            shape='triangulo' 
       elif(sides==4): 
             x,y,w,h=cv2.boundingRect(cnt)
             aspectratio=float(w)/h 
             if (aspectratio==1):
                   shape='cuadrado'                   
             else:
                   shape="rectangulo"                   
       elif(sides==5):
            shape='pentagono'            
       elif(sides==6):
            shape='hexagono'            
       elif(sides==8): 
            shape='octagono'            
       elif(sides==10): 
            shape='estrella'            
       else:
           shape='circulo'          
           
       return shape

    
for cnt in contours:
    moment=cv2.moments(cnt) 
    cx = int(moment['m10'] / moment['m00']) 
    cy = int(moment['m01'] / moment['m00']) 
    shape=detectShape(cnt)
    cv2.drawContours(img,[cnt],-1,(0,255,0),2)
    cv2.putText(img,shape,(cx,cy),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)  #para colocar el numero de lados del poligono .
    cv2.imshow('pioligono detectado',img)
    
    
cv2.waitKey(0) 
cv2.destroyAllWindows()
