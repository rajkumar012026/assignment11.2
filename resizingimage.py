'''
The program is written to resize image
'''


import cv2

image_path = 'nature1.jpg'

img = cv2.imread(image_path)

# Check if images were loaded successfully
if img is None:
    print(f"Error: Could not load the image from {image_path}. Please check the path and file.")
else:
    height, width, _ = img.shape
    print(f"Image original size is : {width}x{height}")
    #resizing the image
    cust_size = (250,200) #width,height by dimension
    cust_img_size = cv2.resize(img,cust_size,interpolation = cv2.INTER_AREA)
    print(f"The image is resized by dimension: {cust_img_size[1]}x{cust_img_size[0]}")
    #resizing by scaling factor
    scaled_img = cv2.resize(img,(0,0),fx=.5,fy=.5,interpolation = cv2.INTER_AREA)
    print(f"The image is resized by scaling factor (.5): {scaled_img.shape[1]}x{scaled_img.shape[0]}")
    cv2.imshow('Original Image', img)
    cv2.imshow('Resized Image by dimension', cust_img_size)
    cv2.imshow('Resized Image by scale',  scaled_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()