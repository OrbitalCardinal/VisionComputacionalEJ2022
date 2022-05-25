import sys
import numpy as np
import cv2
# with open('test.txt', 'w+') as file:
#     file.write('test')


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

node_input = sys.argv[1]
if node_input == 'undefined':
    print('UNDEFINED PATH')
else:
    image = open_img(node_input)
    image_gray = gray_scale(image)
    filename = node_input.split('\\')[-1].split('.')[0]
    path = f'./processed_images/{filename}-gray.png'
    cv2.imwrite(path, image_gray)
    print(path)
