import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('image_secretA_B_gris.bmp') #Image en niveau de gris

def inverse(pixel):
    return 255-pixel

def negatif(img):
    nouvelle_image = np.zeros((img.shape[0]//2, img.shape[1]), dtype='uint8') #Seulement la partie supérieur de l'image est convertie
    for i in range(nouvelle_image.shape[0]):
        for j in range(nouvelle_image.shape[1]):
            nouvelle_image[i, j] = inverse(img[i, j])[0]

    plt.imsave("image_secretA_B_inverse.bmp", nouvelle_image, cmap="gray")

negatif(img)
