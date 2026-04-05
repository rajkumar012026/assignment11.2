'''
The program is written to bilaterally filter the image
'''
import cv2

image_path = 'nature1.jpg'
img1 = cv2.imread(image_path)
desired_size = (600,600)#resize dimension
img = cv2.resize(img1,desired_size,interpolation = cv2.INTER_AREA)
if img is None:
    print('Error: The image was not loaded')
else:
    bilat_filtered_img = cv2.bilateralFilter(img, d=59,sigmaColor=75,sigmaSpace=75)

    cv2.imshow('Original image', img)
    cv2.imshow('Bilateral filtered image', bilat_filtered_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()