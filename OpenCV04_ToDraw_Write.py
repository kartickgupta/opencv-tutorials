# To draw and write on images
# ! all color in BGR
import cv2
import numpy as np

img = cv2.imread('python/OpenCV/1', cv2.IMREAD_UNCHANGED)

# line(on what, starting(x,y), ending(x,y), color, width)
cv2.line(img, (20, 20), (4000, 7000), (255, 0, 0), 5)

# circle(on what, center(x,y), radius, color, width)
cv2.circle(img, (750, 800), 500, (145, 200, 50), 4)

# Using pixel width = -1, fills it completly
cv2.circle(img, (1150, 100), 50, (255, 0, 255), -1)

#rectangle(on what, right-top corner(x,y), left-bottom-corner(x,y), width)
cv2.rectangle(img, (0, 0), (700, 700), (0, 255, 0), 4)

# For Polygon 
# 1. decide pts and convet into np array

pts = np.array([[1000,50],[200,300],[700,200],[500,100]], np.int32)
print(pts.ndim)
# pts = pts.reshape((-1,1,2)) -- OPtional just in documentation
# polylines(on what, [pts], join last and first point ?, color, width)----- no filling option)
cv2.polylines(img, [pts], True, (0, 0, 255), 5)

#     Text select font
font = cv2.FONT_HERSHEY_SIMPLEX
# putText(on what, 'Text', STarting pt, font, font size, color, width, anti-aliasing(for smoothening) )
cv2.putText(img, 'OpenCV Rccks!', (400, 700), font, 3, (200, 255, 155), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()