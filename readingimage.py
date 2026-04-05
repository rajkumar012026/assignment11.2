'''
The program is written to read image
'''


import cv2

image_path = 'nature1.jpg'

img_color = cv2.imread(image_path, cv2.IMREAD_COLOR)
img_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if images were loaded successfully
if img_color is None:
    print(f"Error: Could not read the image from {image_path}. Please check the path and file.")
else:
    print(f"Color Image Shape: {img_color.shape}")
    print(f"Grayscale Image Shape: {img_gray.shape}")
    cv2.imshow('Original Color Image', img_color)
    cv2.imshow('Grayscale Image', img_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()