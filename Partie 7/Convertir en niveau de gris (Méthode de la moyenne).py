import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('image_secretA_B.bmp') #Format .bmp

def niveau_de_gris(pixel):
    return int((max(pixel)+min(pixel))/2)

def gris(img):
    nouvelle_image = np.zeros((img.shape[0], img.shape[1]), dtype='uint8')
    for i in range(nouvelle_image.shape[0]):
        for j in range(nouvelle_image.shape[1]):
            nouvelle_image[i, j] = niveau_de_gris(img[i, j])

    plt.imsave("image_secretA_B_gris.png", nouvelle_image)

gris(img)
