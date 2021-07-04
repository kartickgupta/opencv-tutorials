# to output videos
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Defining the Codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Definig output function
out = cv2.VideoWriter('kartick.avi', fourcc, 20.0, (640, 480))
#                       ('name.ext', codec, fps, dimension in tuple)

while True:
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()