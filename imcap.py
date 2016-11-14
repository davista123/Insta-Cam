import cv2
import numpy as np 

font = cv2.FONT_HERSHEY_SIMPLEX

vid = cv2.VideoCapture(0)
while(True):
	_, frame = vid.read()
	cv2.imshow('frame', frame)
	cv2.putText(frame,'Hello World!',(10,500), font, 1,(255,255,255),2)
	if cv2.waitKey(1) & 0xFF == ord('s'):
		cv2.imwrite("frame.jpg",frame)
		break
vid.release()
cv2.destroyAllWindows()
