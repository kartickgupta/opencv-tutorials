import cv2
import numpy as np

img = cv2.imread('/home/kartickgupta/Kartick/CoderForNow/python/OpenCV/1', cv2.IMREAD_COLOR)

# selecting a px as img is a 2D array 
# img[y,x] making it while coloured
px = img[900, 600] = [255, 255, 255]
cv2.circle(img, (600, 900), 50, (0, 0, 255), 3)
print(px)

# similarly making ROI, Reigon of Image = white
img[400:800, 400:800] = [225, 225, 225]

# Taking away Jordan's Face
jordan_face = img[ 200:600, 600:800]
# the shape of an array is a tuple of integers giving the size of the array along each dimension.
print(jordan_face.shape)


#SUper imposing it on image
img[0:400, 0:200] = jordan_face


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
