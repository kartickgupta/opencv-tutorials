# Thresholding -- brings more clearity


import cv2
import numpy as np

img = cv2.imread('/home/kartickgupta/Kartick/CoderForNow/python/OpenCV/book', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# thresholding can do, at the most basic level, 
# is convert everything to white or black, 
# based on a threshold value.

#On Colored
retval, threshold = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)
                   #cv2.threshold(on what, thresholdValue, MaxValue, typeOfThreshold)

# On GrayScale
retvalG, thresholdG = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)





# adaptive thresholding. It uses the algorithm that calculates the threshold for a small regions of the image so that we can get different thresholds for different regions of the same image and it gives us better results for images with varying light conditions.

th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
                            #         cv2.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood values where weights are a gaussian window.


cv2.imshow('th',th)
cv2.imshow('thresholdG', thresholdG)
cv2.imshow('threshold', threshold)
cv2.imshow('gray', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()