# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 10:01:16 2020

@author: zefyr
Includes code adapted from:
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html#contour-features
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html#converting-colorspaces
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
"""

import cv2
import numpy as np



cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,80,80])
    upper_blue = np.array([140,255,255])
    
    # # define range of blue color in BGR
    # lower_blue = np.array([79,63,55])
    # upper_blue = np.array([255,0,85])
    

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    # #new stuff
    ret,thresh = cv2.threshold(res,150,255,0)
    b,g,r = cv2.split(thresh)
    contours,hierarchy = cv2.findContours(b+g+r, 1, 2)
    if(len(contours)!=0):
        # # "biggest" contour, based on num of points in contour
        maxc = 0
        for i in range(len(contours)):
            c = len(contours[i])
            if c>maxc:
                maxc = c
                cntb = contours[i]
        
        # # "biggest" contour, based on area of contour. Seems to work worse
        # maxa = 0
        # for i in range(len(contours)):
        #     a = cv2.contourArea(contours[i])
        #     if a>maxa:
        #         maxc = a
        #         cnta = contours[i]
           
        x,y,w,h = cv2.boundingRect(cntb)
        res = cv2.rectangle(res,(x,y),(x+w,y+h),(0,255,0),2)
        
        # # View all contours at once
        # for i in range(len(contours)):
        #     x,y,w,h = cv2.boundingRect(contours[i])
        #     res = cv2.rectangle(res,(x,y),(x+w,y+h),(0,255,0),2)

    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()