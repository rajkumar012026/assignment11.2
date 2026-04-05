'''
The program is written to save the image
'''


import cv2

image_path = 'nature1.jpg'

img = cv2.imread(image_path, cv2.IMREAD_COLOR)

if img is None:
    print(f"Error: Image not loaded for writing.")
else:
    #Saving the original image as PNG file
    output_path_png = 'image/output_image.png'
    cv2.imwrite(output_path_png, img)
    print(f"Image saved as {output_path_png}")
    #converting the image to grayscale and save as JPEG file
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    output_path_gray_jpeg = 'image/output_gray_jpeg.jpg'
    cv2.imwrite(output_path_gray_jpeg, img_gray)
    print(f"Grayscale image saved as {output_path_gray_jpeg}")
    cv2.imshow('PNG file', cv2.imread(output_path_png))
    cv2.imshow('JPEG file', cv2.imread(output_path_gray_jpeg))
    cv2.waitKey(0)
    cv2.destroyAllWindows()