import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

def open_img(path):
    img_bgr2 = cv2.imread(path)
    img_rgb = cv2.cvtColor(img_bgr2, cv2.COLOR_BGR2RGB)
    return img_rgb

def gray_scale(img, frac = 1/3): 
    # Dimensiones de la imagen original
    dim = img.shape
    # Nuevo arreglo bidimensional
    img_gray = np.zeros((dim[0], dim[1]))
    # Valor de intensidad con fraccion
    for i in range(dim[0]):
        for j in range(dim[1]):
            new_r = img[i,j,0] * frac
            new_g = img[i,j,1] * frac
            new_b = img[i,j,2] * frac
            new_val = new_r + new_g + new_b
            img_gray[i,j] = np.ceil(new_val)
    return img_gray

def show_img(img, colormode = 'gray'):
    dim = img.shape
    colormap = 'gray' if len(dim) < 3 else None
    colormode = 'L' if len(dim) < 3 else 'RGB'
    img = Image.fromarray(np.uint8(img), colormode)
    plt.imshow(img, colormap)
    plt.axis('off')
    plt.show()
    
def increase_brightness(img,  beta, correct = False):
    # ACLARAR IMAGEN
    img = img.copy()
    dim = img.shape
    for i in range(dim[0]):
        for j in range(dim[1]):
            img[i,j] = img[i,j] + beta
    
    # CORRECCION DE EXCESO DE RANGO
    if correct:
        max_ = np.max(img)
        min_ = np.min(img)
        correct_up = False
        correct_down = False
        for i in range(dim[0]):
            for j in range(dim[1]):
                if img[i,j] > 255:
                    img[i,j] = (img[i,j] / max_) * 255
                if img[i,j] < 0:
                    img[i,j] = img[i,j] + np.abs(min_)
    return img