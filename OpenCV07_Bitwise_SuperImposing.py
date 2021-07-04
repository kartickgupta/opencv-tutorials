# Image SuperImposing and Thresholding
import cv2
import numpy as np

img1 = cv2.imread('/home/kartickgupta/Kartick/CoderForNow/python/OpenCV/1', cv2.IMREAD_COLOR)
img2 = cv2.imread('/home/kartickgupta/Kartick/CoderForNow/python/OpenCV/2', cv2.IMREAD_COLOR)

rows, columns, channels = img2.shape
roi = img1[0:rows, 0:columns]

# Now create a mask of logo and create its inverse mask
img2Gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
#cv2.imshow('img2Gray', img2Gray)

# add a threshold
ret, mask = cv2.threshold(img2Gray, 230, 255, cv2.THRESH_BINARY_INV)
# selecting evrything b/w 230 and 255 all rest will be black



mask_inv = cv2.bitwise_not(mask)
#cv2.imshow('mask_inv', mask_inv)


# Now black-out the area of logo in ROI og img1
img1_bg = cv2.bitwise_and(roi, roi, mask= mask_inv)
#cv2.imshow('img1_bg', img1_bg)




# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2, img2, mask= mask)
#cv2.imshow('img2_fg', img2_fg)

dst = cv2.add(img1_bg, img2_fg)

img1[0:rows, 0:columns] = dst

# cv2.imshow('result', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

