import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('image_secretA_B.bmp') #Format .bmp

def niveau_de_gris_methode1(pixel):
    return int((max(pixel)+min(pixel))/2)

def niveau_de_gris_methode2(pixel):
    return 0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2]

def gris(img):
    nouvelle_image = np.zeros((img.shape[0], img.shape[1]), dtype='uint8')
    for i in range(nouvelle_image.shape[0]):
        for j in range(nouvelle_image.shape[1]):
            nouvelle_image[i, j] = niveau_de_gris_methode1(img[i, j])

    plt.imsave("image_secretA_B_gris.png", nouvelle_image, cmap="gray")

gris(img)
