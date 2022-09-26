import cv2 as cv
import numpy as np
vid=cv.VideoCapture(0)
blank=np.zeros((500,500,3),dtype='uint8') #heigth,width,no_of_colorchannels

blank[:]=255,0,0 		#blue,green,red --->	b g r  
blank[200:300,300:400]=0,255,0 		#blue,green,red --->	b g r  
# cv.rectangle(blank,(0,0),(250,500),(0,0,255),thickness=cv.FILLED)
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,0,255),thickness=cv.FILLED)

#to draw a circle

cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,255,0),thickness=-1)

#to draw a line

# cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=3)
cv.line(blank,(0,250),(blank.shape[1],blank.shape[0]//2),(255,255,255),thickness=3)


#write a text on image

cv.putText(blank,'hello',(200,400),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,255),2)




cv.imshow('blank',blank)
cv.waitKey(0)

def resizeFrame(frame,scale=0.75):
	width=int(frame.shape[1]*scale)
	height=int(frame.shape[0]*scale)
	dimensions=(width,height)

	return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeRes(width,height):
	#live video
	capture.set(3,width)
	capture.set(4,height)



while(True):
	ret,frame=vid.read()
	frame_resized=resizeFrame(frame,scale=0.2)

	cv.imshow('video',frame)
	cv.imshow('resizedframe',frame_resized)
	if(cv.waitKey(1) & 0xFF == ord('q')):
		break
	
	# if(cv.waitKey(1)==ord('q')):
	# 	break
vid.release()
cv.destroyAllWindows()