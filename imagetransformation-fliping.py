'''
The program is written to transform the image
'''
import cv2
import numpy as np

image_path = 'nature1.jpg'

img = cv2.imread(image_path)

if img is None:
    print("Error: Image not loaded for flipping.")
else:
    # Flip horizontally
    flipped_h = cv2.flip(img, 1)
    # Flip vertically
    flipped_v = cv2.flip(img, 0)
    # Flip both horizontally and vertically
    flipped_hv = cv2.flip(img, -1)
    cv2.imshow('Original', img)
    cv2.imshow('Flipped Horizontally', flipped_h)
    cv2.imshow('Flipped Vertically', flipped_v)
    cv2.imshow('Flipped Both', flipped_hv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()