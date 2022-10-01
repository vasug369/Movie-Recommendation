import cv2 as cv
import numpy as np
vid=cv.VideoCapture(0)
while(True):
	isTrue,frame=vid.read()
	blank=np.zeros(frame,dtype=uint8)
	cv.imshow('myvideo',frame)
	if(cv.waitKey(1) & 0xFF==ord('q')):
		break
vid.release()
cv.destroyAllWindows()
