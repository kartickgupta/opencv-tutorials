# Template MAtching
import cv2
import numpy as np

img = cv2.imread('/home/kartickgupta/Kartick/CoderForNow/python/OpenCV/opencv-template-matching-python-tutorial.jpg', 1)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread('/home/kartickgupta/Kartick/CoderForNow/python/OpenCV/opencv-template-for-matching.jpg',0)

w, h = template.shape[::-1]
# the shape of an array is a tuple of integers giving the size of the array along each dimension.

# returns an Gray image with white dots, resepresenting starting of template to b e matched
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
# returns array of matching values
threshold = 0.8


# returns array of pts where condtion holds true
loc = np.where(res >= threshold)




for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1]+h), (0, 255, 255), 1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, "Found",(pt[0], pt[1]+h+10), font, 0.5, (0,255, 255),1, cv2.LINE_AA)

    

# cv2.imshow('res', res)  
cv2.imshow('Detected', img)
cv2.waitKey(0)
cv2.destroyAllWindows()