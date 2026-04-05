'''
The program is written to remove noise from an image by using median blur algorithm.
'''
import cv2
import numpy as np
#Reading and resizing the image as to fit on desktop screen
img_org = cv2.imread('nature1.jpg')
img = cv2.resize(img_org, (300, 300))
if img is None:
    print("Error: Image not loaded for median blur example.")
else:
    # Adding artificial noise to the image
    # Adding randomly dark or light pixels
    noisy_img = np.copy(img)
    num_salt = int(0.01 * img.size)
    coords = [np.random.randint(0, i - 1, num_salt) for i in img.shape]
    noisy_img[coords[0], coords[1], :] = 255
    num_pepper = int(0.01 * img.size)
    coords = [np.random.randint(0, i - 1, num_pepper) for i in img.shape]
    noisy_img[coords[0], coords[1], :] = 0

    # Applying Median Blur technique to remove noise with a 5x5 kernel (Aperture)
    median_blurred_img = cv2.medianBlur(noisy_img, 5)
    #Showing the images
    cv2.imshow('Original image', img)
    cv2.imshow('Original Noisy Image', noisy_img)
    cv2.imshow('Median Blurred (5x5)', median_blurred_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()