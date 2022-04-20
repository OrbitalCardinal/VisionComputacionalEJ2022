from cv2 import cv2
import itertools
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def open_img(path):
    img_bgr2 = cv2.imread(path)
    img_rgb = cv2.cvtColor(img_bgr2, cv2.COLOR_BGR2RGB)
    return img_rgb


def show_img(img, colormode='gray'):
    dim = img.shape
    colormap = 'gray' if len(dim) < 3 else None
    colormode = 'L' if len(dim) < 3 else 'RGB'
    img = Image.fromarray(np.uint8(img), colormode)
    plt.imshow(img, colormap)
    plt.axis('off')
    plt.show()


def euclidean_norm(vec):
    vec_squared = np.square(vec)
    sum_squared = np.sum(vec_squared)
    sum_sqrt = np.sqrt(sum_squared)
    return sum_sqrt


img = open_img('../test_imgs/orange_blasco.png')
print('IMAGE SHAPE', img.shape)

# PEER GROUP
test = np.floor(np.random.rand(10, 10, 3) * 255)

print('TEST SHAPE', test.shape)

# DISJOINT BLOCKS PARTITIONS
n = 3  # Window size

# Corner window values
c_values1 = [i*n for i in range(test.shape[0] // n)]
c_values2 = [((i+1)*n) - 1 for i in range(test.shape[0] // n)]

# Corner window combinations
x1y1 = list(itertools.product(c_values1, repeat=2))
x2y2 = list(itertools.product(c_values2, repeat=2))

print(x1y1)
print(x2y2)
show_img(test)

# Save disjoint blocks
blocks = []
for i in range(len(x1y1)):
    blocks.append(test[x1y1[i][0]:x2y2[i][0]+1, x1y1[i][1]:x2y2[i][1]+1])
    show_img(test[x1y1[i][0]:x2y2[i][0]+1, x1y1[i][1]:x2y2[i][1]+1])

# MEMBERS OF PEER GROUP
d = 1  # DISTANCE
xi = np.array([5, 6, 9])
xj = np.array([4, 5, 8])
distance_btw = euclidean_norm(xi) - euclidean_norm(xj)
is_member = distance_btw <= d
print(is_member)
