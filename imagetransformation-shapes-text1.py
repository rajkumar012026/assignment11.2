'''
The program is written to create shape and add text to it
'''
import cv2
import numpy as np

image_path = 'nature1.jpg'
img = cv2.imread(image_path)
img_resized = cv2.resize(img, (800,750))
#Creating a blank image
img_blank = np.zeros((800,750))
#Drawing a rectangular shape on the existing image of the size of the image of red color
height = img_resized.shape[0]
width = img_resized.shape[1]

cv2.rectangle(img_resized,(0,0),(width-1,height-1),(255,0,0),5)
#Circle within rectangle on the image
if height < width:
    radius = (height-3) // 2
else:
    radius = (width-3) // 2
center = (width//2, height//2)


cv2.circle(img_resized,center,radius,(0,0,255),5)
#drawing a filled yellow circle in red circle
cv2.circle(img_resized,center,radius//2,(0,255,255),-1)
#Draw a line across the image
cv2.line(img_resized,(0,height//2),(width,height//2),(0,55,255),5)
#showing blank image

cv2.imshow('Blank Image', img_blank)
#Put a text on filled circle
cv2.putText(img_resized,'Adding text on an image',((width//2)-radius,(height//2)-4),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,250,0),2,cv2.LINE_AA)
cv2.imshow('Original Image', img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
import numpy as np
import cv2

# Create a blank image (height=300, width=500)
img = np.zeros((300, 500, 3), dtype=np.uint8)

# Get dimensions
height, width = img.shape[:2]

# Draw a rectangle covering the entire image
# pt1 is top-left (0,0), pt2 is bottom-right (width-1, height-1)
cv2.rectangle(img, (0, 0), (width - 1, height - 1), (0, 255, 0), 5)

print(f"Image shape: {img.shape}")
print(f"Rectangle drawn from (0,0) to ({width-1}, {height-1})")
cv2.imshow('Original Image', img)
cv2.waitKey(0)
'''