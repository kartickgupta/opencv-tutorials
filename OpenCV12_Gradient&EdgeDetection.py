# Image Gradient and Canny Edge Detection

import cv2
import numpy as np

cam = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('edge.avi', fourcc, 20.0, (640, 480))

while True:
    _, frame = cam.read()

#     Gradients
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)  # CV_64F is a data type
    # (on what, data type, X Value, Y Value, Kernel size)
    sobelX = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    sobelY = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)

#     Edge Detection
    edges = cv2.Canny(frame, 100, 150)
#     out.write(edges)

#     cv2.imshow('laplacian', laplacian)
#     cv2.imshow('sobelX', sobelX)
#     cv2.imshow('sobelY', sobelY)
    cv2.imshow('edges', edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
# out.release()
cv2.destroyAllWindows()
