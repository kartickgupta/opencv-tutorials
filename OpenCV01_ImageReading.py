import cv2
import numpy as np
from matplotlib import pyplot as plt



imgLocation = 'python/OpenCV/1'

# to read an colored image in grayscale
# IMREAD_GRAYSCALE = 0
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1

img = cv2.imread(imgLocation,cv2.IMREAD_UNCHANGED)

# To display image
cv2.imshow('Jordan Belford',img)

cv2.waitKey(0) # To wait for - milliseconds after image opening

# imwrite('name.ext', img) to the save the image in working directory
cv2.imwrite('2.png', img)

cv2.destroyAllWindows()