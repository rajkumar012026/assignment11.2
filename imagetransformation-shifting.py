'''
The program is written to shift the image
'''
import cv2
import numpy as np
image_path = 'nature1.jpg'
img = cv2.imread(image_path)
if img is None:
    print("Error: Image not loaded for shifting.")
else:
    height, width, _ = img.shape
    # Define the amount to shift (tx, ty)
    # Shift 100 pixels right, 50 pixels down
    tx, ty = 100, 50
    # Create the 2x3 translation matrix
    M = np.float32([[1, 0, tx], [0, 1, ty]])
    # Apply the affine transformation
    shifted_img = cv2.warpAffine(img, M, (width, height))  # Output size same as original

    cv2.imshow('Original', img)
    cv2.imshow(f'Shifted by ({tx},{ty})', shifted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()