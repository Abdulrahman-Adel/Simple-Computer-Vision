# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 03:50:22 2020

@author: Abdelrahman
"""
#import numpy as np
import cv2

highThresh	= 0.4
lowThresh		= 0.1

def sobel (img):
	'''
	Detects edges using sobel kernel
	'''
	opImgx		= cv2.Sobel(img,cv2.CV_8U,0,1,ksize=3)	#detects horizontal edges
	opImgy		= cv2.Sobel(img,cv2.CV_8U,1,0,ksize=3)	#detects vertical edges
	#combine both edges
	return cv2.bitwise_or(opImgx,opImgy)	#does a bitwise OR of pixel values at each pixel

def sketch(frame):	
	#Blur it to remove noise
	frame		= cv2.GaussianBlur(frame,(3,3),0)
	
	#make a negative image
	invImg	= 255-frame
	
	#Detect edges from the input image and its negative
	edgImg0	= sobel(frame)
	edgImg1	= sobel(invImg)
	edgImg	= cv2.addWeighted(edgImg0,1,edgImg1,1,0)	#different weights can be tried too
	
	#Invert the image back
	opImg	= 255-edgImg
	return opImg
	
if __name__ == '__main__':
    
    img	= cv2.imread("img.jpg",0)
    #img = cv2.resize(img,(600,600))
    opImg = sketch(img)	
    cv2.imwrite("../Basic Computer Vision/Sketch_Image.jpg",opImg)
    #cv2.imshow("Sketch",opImg)
	
cv2.waitKey()
cv2.destroyAllWindows()


