'''
The program is written to rotate the image
'''
#importing the library
import cv2


image_path = 'nature1.jpg'
img1 = cv2.imread(image_path)
img = cv2.resize(img1, (400,400))

if img is None:
    print("Error: Image not loaded.")
else:
    height, width, _ = img.shape
    #Finding the center of the image
    center = (width // 2, height // 2)
    angle = 45
    scale = 1.0
    #rotating the image by 45 degree anticlockwise with original image scale
    matrix_45 = cv2.getRotationMatrix2D(center, angle, scale)
    rotatedbyangle_45 = cv2.warpAffine(img, matrix_45, (width, height))
    # rotating the image by 90 degrees clockwise with half scale of the original
    angle_neg = -90
    scale_half = 0.5
    matrix_neg_90 = cv2.getRotationMatrix2D(center, angle_neg, scale_half)
    rotated_neg_90 = cv2.warpAffine(img, matrix_neg_90, (width, height))
    cv2.imshow('Original image', img)
    cv2.imshow(f'Rotated image by {angle} anticlockwise degrees', rotatedbyangle_45)
    cv2.imshow(f'Rotated image {angle_neg} degrees clockwise',rotated_neg_90)
    cv2.waitKey(0)
    cv2.destroyAllWindows()