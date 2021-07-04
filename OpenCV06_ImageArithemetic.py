# Image Arithemaetic
import cv2 
import numpy as np

twitter = cv2.imread('/home/kartickgupta/Kartick/CoderForNow/python/OpenCV/twitter.png', cv2.IMREAD_COLOR)
sun =  cv2.imread('/home/kartickgupta/Kartick/CoderForNow/python/OpenCV/sun.png', cv2.IMREAD_COLOR)

img = sun + twitter
sub = sun - twitter

#in-built addition
add = cv2.add(sun, twitter)

#blending of 2 images          alpha         beta  gamma == 0 Always
weighted = cv2.addWeighted(sun, 0.7, twitter, 0.3, 0)

cv2.imshow('weighted Sum', weighted)
# cv2.imshow('Open CV add', add)
# cv2.imshow('sub', sub)
# cv2.imshow('sum', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
