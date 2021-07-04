# Morphological Transformations ----------- Noise Removal
import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    _, frame = cam.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    yellow_lower = np.array([20, 100, 100])
    yellow_upper = np.array([100, 255, 255])
    
    mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    kernel = np.ones((5,5), np.uint8) # Window
    
    
    
#  Used to remove white noises  it erodes away the boundaries of foreground object. Decreases the white region. The kernel slides through the image (as in 2D convolution). A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1, otherwise it is eroded (made to zero).

    erosion = cv2.erode(mask, kernel, iterations = 1)
   
# It is just opposite of erosion. Used to remove black noises Here, a pixel element is '1' if atleast one pixel under the kernel is '1'. So it increases the white region in the image or size of foreground object increases. Normally, in cases like noise removal, erosion is followed by dilation. Because, erosion removes white noises, but it also shrinks our object. So we dilate it. Since noise is gone, they won't come back, but our object area increases. It is also useful in joining broken parts of an object.

    dilation = cv2.dilate(erosion,kernel,iterations = 1)
    
#     Opening is just another name of erosion followed by dilation. It is useful in removing noise, whites from background
    opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel)
    
#     Closing is reverse of Opening, Dilation followed by Erosion. It is useful in closing small holes inside the foreground objects, or small black points on the  object.
    closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)

    
#     It is the difference between dilation and erosion of an image. The result will look like the outline of the object.
    gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)



#     cv2.imshow('dilation', dilation)
#     cv2.imshow('erode', erosion)
#     cv2.imshow('res', mask)
#     cv2.imshow('opening', opening)
#     cv2.imshow('gradient', gradient)
    cv2.imshow('closing', closing)




    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cam.release()
cv2.destroyAllWindows()