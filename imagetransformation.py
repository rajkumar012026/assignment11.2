'''
The program is written to transform the image
'''
import cv2
import numpy as np

image_path = 'nature1.jpg'
#Convert to grayscale for binary operations
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print(f"Error: Image not loaded for morphological operations.")
else:
    #convert to binary image
    _, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    #5x5 rectangular kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    # Erosion
    eroded_img = cv2.erode(binary_img, kernel, iterations = 1)
    #Dilation
    dilated_img = cv2.dilate(binary_img, kernel, iterations = 1)
    #Opening
    opened_img = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, kernel)
    #closing
    closed_img = cv2.morphologyEx(binary_img, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('Original binary', binary_img)
    cv2.imshow('Eroded', eroded_img)
    cv2.imshow('Dilated', dilated_img)
    cv2.imshow('Opened', opened_img)
    cv2.imshow('Closed', closed_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()