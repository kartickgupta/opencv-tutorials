# Image Blurring and Smoothening

import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    _, frame = cam.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    yellow_lower = np.array([20, 100, 100])
    yellow_upper = np.array([30, 255, 255])
    
    mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
#   Making kernel (Window for applying LPFs)
    kernel = np.ones((15, 15), np.float32)/225
#     print(kernel)
    
    
    # 2D - Filter -- Normal Box Filter
    
    # Filtering with the above kernel results in the following being performed: for each pixel, a 5x5 window is centered on this       pixel, all pixels falling within this window are summed up, and the result is then divided by 25. This equates to              computing the average of the pixel values inside that window.

    smoothening = cv2.filter2D(res, -1, kernel)
#     cv2.imshow('smoothening', smoothening)
    
    
    
    
    # Blurring
    
    
    # Averaging
    
    #     It simply takes the average of all the pixels under 
    #     kernel area and replaces the central element with this average. 

    blur = cv2.blur(res, (5,5))
#     cv2.imshow('blur', blur)
    
    
    #     Works on the baisis of Gaussian Function, weight as decreases 
    #     as we go away from the pixel on which it's computed and value gets replaced
    #     takes image, kernel size(Width & Height) (odd and +ive), Std Deviation in X and Y
    gassian = cv2.GaussianBlur(res, (15, 15), 0)
#     cv2.imshow('gassian', gassian)
    
    
    #     computes the median of all the pixels under the kernel window and 
    #     the central pixel is replaced with this median value. 
    median = cv2.medianBlur(res, 5)
    cv2.imshow('median', median)
    
    
#     cv2.imshow('smoothening', smoothening)
#     cv2.imshow('blur', blur)
#     cv2.imshow('gassian', gassian)
#     cv2.imshow('median', median)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break     

cam.release()
cv2.destroyAllWindows()