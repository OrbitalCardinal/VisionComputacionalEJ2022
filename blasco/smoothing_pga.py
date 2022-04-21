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

# print(x1y1)
# print(x2y2)
# show_img(test)

# Save disjoint blocks
blocks = []
for i in range(len(x1y1)):
    blocks.append(test[x1y1[i][0]:x2y2[i][0]+1, x1y1[i][1]:x2y2[i][1]+1])
    # show_img(blocks[i])


# PEER GROUPS
# print(blocks[0])

peer_groups = []
d = 1
for i in range(len(blocks)):
    xi = np.array([
        blocks[i][0, n // 2, n // 2],
        blocks[i][1, n // 2, n // 2],
        blocks[i][2, n // 2, n // 2]
        ])  # Central pixel
    flatten = blocks[i].reshape(n, - 1)
    # print('CENTRAL PIXEL', xi)
    xi_peer_group = []
    for j in range(flatten.shape[1]):
        xj = np.array([flatten[0, j], flatten[1, j], flatten[2, j]])
        # print(xj)

        # MEMBERS OF PEER GROUP
        distance_btw = euclidean_norm(xi) - euclidean_norm(xj)
        is_member = distance_btw <= d
        if is_member:
            xi_peer_group.append(())
    peer_groups.append(xi_peer_group)

# DETECTION PROCEDURE
# print('DETECTION PROCEDURE')

m = 1
for i in range(len(blocks)):
    pg_cardinality = len(peer_groups[i])
    is_non_corrupted = pg_cardinality >= (m + 1)
    







