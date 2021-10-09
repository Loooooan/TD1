import numpy as np

img = plt.imread('image_secretA_B.bmp') #Format .bmp

def retrecissement(img):
    nouvelle_image = np.zeros((img.shape[0]//2, img.shape[1]//2, 3), dtype='uint8')
    for i in range(nouvelle_image.shape[0]):
        for j in range(nouvelle_image.shape[1]):
            nouvelle_image[i, j] = img[2*i, 2*j]
    plt.imsave("image_secretA_B_retrecie.png", nouvelle_image)

retrecissement(img)
