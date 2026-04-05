'''
The program is written to implement laplacian operator
which is used to highlight the regions with rapid intensity
'''
import cv2
import numpy as np
try:
    #reading , changing to grayscale and resize the dimension of the image
    img_org = cv2.imread('nature1.jpg',cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img_org, (300, 300))
except FileNotFoundError:
    print("Error: Image not loaded for Sobel/Laplacian.")
else:
    #Sobel operator used to computes the gradient magnitude in X direction
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    # Convert the image back to 8-bit
    sobel_x = np.uint8(np.absolute(sobel_x))
    #Sobel operator used to computes the gradient magnitude in Y direction
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    # Convert the image back to 8-bit
    sobel_y = np.uint8(np.absolute(sobel_y))
    #combine both the gradients in magnitude
    sobel_combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
    # Laplacian operator to highlight the rapid intensity
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    # Convert the image back to 8-bit
    laplacian = np.uint8(np.absolute(laplacian))

    cv2.imshow('Original Grayscale image', img)
    cv2.imshow('Sobel in X direction', sobel_x)
    cv2.imshow('Sobel in Y direction', sobel_y)
    cv2.imshow('Combined', sobel_combined)
    cv2.imshow('Laplacian', laplacian)
    cv2.waitKey(0)
    cv2.destroyAllWindows()