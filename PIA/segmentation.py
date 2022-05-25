from matplotlib.pyplot import show


def main(path, k):
    from cv2 import cv2
    import itertools
    import numpy as np
    import matplotlib.pyplot as plt
    from PIL import Image
    import time
    from IPython.display import clear_output
    import sys

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
        
    # ABRIR IMAGEN
    img = open_img(path)

    # SUAVIZADO
    dst = cv2.fastNlMeansDenoisingColored(img, None, 5, 5, 4, 10)

    # SEGMENTACION
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    pixel_values = dst.reshape((-1, 3))
    pixel_values = np.float32(pixel_values)
    k = int(k)
    _, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # RECONSTRUCCION CON SEGMENTACION
    centers = np.uint8(centers)
    labels = labels.flatten()
    segmented_image = centers[labels.flatten()]

    # reshape back to the original image dimension
    segmented_image = segmented_image.reshape(dst.shape)
    show_img(segmented_image, 'L')
    cv2.imwrite('segmentacion.png' ,segmented_image)


