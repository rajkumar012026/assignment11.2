'''
The program is written to resize the image in terms of its ratio
'''
import cv2

#Reading an image
img_path = 'nature1.jpg'
img = cv2.imread(img_path)

if img is None:
    print('Could not open or find the image')
else:
    org_height = img.shape[0]
    org_width = img.shape[1]

    #ration of size of original shape/image
    img_size_ratio = org_width/org_height
    #new image size with respect to its width
    new_width = 500
    new_height = int(new_width / img_size_ratio)
    new_dim_by_width = (new_width, new_height)
    resized_img_new_by_width = cv2.resize(img,new_dim_by_width,interpolation = cv2.INTER_AREA)
    #new image size with respect to its height
    new_height1 = 400
    new_width1 = int(new_height1 * img_size_ratio)
    resize_img_by_height = cv2.resize(img,(new_width1,new_height1),interpolation = cv2.INTER_AREA)
    #Showing the image
    cv2.imshow('Original Image',img)
    cv2.imshow(f'Resized Image by width {new_width} in the ratio',resized_img_new_by_width)
    cv2.imshow(f'Resized Image by height {new_height1} in the ratio',resize_img_by_height)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
