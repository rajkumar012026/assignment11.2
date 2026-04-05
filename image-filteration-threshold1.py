'''
The program is written to threshold the image - Image filtration
'''
import cv2

image_path = 'nature1.jpg'

try:
    img1 = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # As the thresholding of image works better on grayscale
    img = cv2.resize(img1, (300, 300))  #resizing before processing filtration as the same can be seen on the window
except FileNotFoundError as e:
    print(f'Error: {e}')
    exit
else:
    threshold_value = 120
    max_value = 200

    #binary thresholding if threshold value is between pixel and max value else 0
    _, th_binary = cv2.threshold(img, threshold_value, max_value, cv2.THRESH_BINARY)
    #binary threshold if threshold is between pixel and 0 else max_value
    _, th_binary_inv = cv2.threshold(img, threshold_value, max_value, cv2.THRESH_BINARY_INV)
    #Threshold if pixel>threshold>threshold else pixel
    _, th_truncate = cv2.threshold(img, threshold_value, max_value, cv2.THRESH_TRUNC)
    # Zero thresholding if pixel > threshold >pixel else 0
    _, th_zero = cv2.threshold(img, threshold_value, max_value, cv2.THRESH_TOZERO)
    # inverse zero threshold
    _, th_zero_inverse = cv2.threshold(img, threshold_value, max_value, cv2.THRESH_TOZERO_INV)
    #Optimal thresholding
    _, th_optimal = cv2.threshold(img, threshold_value, max_value, cv2.THRESH_OTSU)



    cv2.imshow('Original grayscale image', img)
    cv2.imshow('Binary thresholded grayscale image', th_binary)
    cv2.imshow('Binary_inv thresholded grayscale image', th_binary_inv)
    cv2.imshow('Truncate thresholded grayscale image', th_truncate)
    cv2.imshow('Zero thresholded grayscale image', th_zero)
    cv2.imshow('Zero inverse thresholded grayscale image', th_zero_inverse)
    cv2.imshow('Optimal thresholded grayscale image', th_optimal)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
