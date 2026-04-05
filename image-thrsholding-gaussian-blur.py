'''
The program is written to blurring the image
'''
import cv2
image_path = 'nature1.jpg'
img_org = cv2.imread(image_path)
img = cv2.resize(img_org, (500, 500))
if img is None:
    print("Error: Image not loaded for Gaussian blur.")
else:
    # Apply Gaussian blur with a 5x5 kernel and sigmaX=0
    blurred_img = cv2.GaussianBlur(img, (5, 5), 0)
    # Apply Gaussian blur with a larger kernel (e.g., 15x15) for more blur
    more_blurred_img = cv2.GaussianBlur(img, (15, 15), 0)
    cv2.imshow('Original', img)
    cv2.imshow('Gaussian Blurred (5x5)', blurred_img)
    cv2.imshow('Gaussian Blurred (15x15)', more_blurred_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()