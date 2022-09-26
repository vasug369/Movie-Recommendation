import cv2 as cv

def rescale_frame(frame,scale=0.75):
	width=int(frame.shape[1]*scale)
	height=int(frame.shape[0]*scale)
	resolution=(width,height)
	return cv.resize(frame,resolution,interpolation=cv.INTER_AREA)

	

img=cv.imread(r"C:\Users\vasug\OneDrive\Pictures\\Camera Roll\WIN_20211107_15_49_19_Pro.jpg")
resize_frame=rescale_frame(img,scale=0.2)
# cv.imshow('image',img)
cv.imshow('image',resize_frame)
cv.waitKey(0)