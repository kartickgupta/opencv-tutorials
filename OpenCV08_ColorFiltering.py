# Colour Filtering
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Hue Saturation Value, differnt colour value depiction
    
    
	yellow_lower = np.array([20, 100, 100])
	yellow_upper = np.array([30, 255, 255]) 
    
    
    # All objects having color range b/w lower and upper will be makred as 0 & 1 
	mask = cv2.inRange(hsv,yellow_lower, yellow_upper)
    
    # Taking and of Original colour and mask all 1's get colored and 0's are blacked out
	final = cv2.bitwise_and(frame, frame, mask = mask)
    
    
	cv2.imshow('mask', mask)	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()

