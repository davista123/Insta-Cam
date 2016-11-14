import cv2
import numpy as np 

vid = cv2.VideoCapture(0)
while(True):
	_, frame = vid.read()
	cv2.imshow('frame', frame)
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(frame,'Press (s) to browse image',(10,500), font, 1, (200,255,155), 2, cv2.LINE_AA)
	if cv2.waitKey(1) & 0xFF == ord('s'):
		cv2.imwrite("frame.jpg",frame)
		break
vid.release()
cv2.destroyAllWindows()
