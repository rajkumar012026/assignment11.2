'''
The program is written to detect edge of the image
'''
import cv2

img_org = cv2.imread('nature1.jpg')
img = cv2.resize(img_org, (600, 600))

if img is None:
    print("Error: Image not loaded.")
else:
    img_edges = cv2.Canny(img, 10, 50)
    img_edges1 = cv2.Canny(img, 20, 100)
    cv2.imshow('Original image', img)
    cv2.imshow('Edged Image with less thresholding', img_edges)
    cv2.imshow('Edged Image with more thresholding', img_edges1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()