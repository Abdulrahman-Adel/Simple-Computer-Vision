# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 02:43:17 2020

@author: Abdelrahman
"""

import cv2


img = cv2.imread("unnamed.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)

_, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)


contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

font = cv2.FONT_HERSHEY_SIMPLEX
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.008*cv2.arcLength(cnt, True), True)
    cv2.drawContours(img, [approx], 0, (0,0,255), 2)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), font, 0.55, (255,0,255))
    elif len(approx) == 4:
        cv2.putText(img, "Rectangle", (x, y), font, 0.55, (255,0,255))
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), font, 0.55, (255,0,255))
    elif 6 < len(approx) < 15:
        cv2.putText(img, "Ellipse", (x, y), font, 0.55, (255,0,255))
    else:
        cv2.putText(img, "Circle", (x, y), font, 0.55, (255,0,255))
    
cv2.imshow("Contour",img)

cv2.imwrite("..\Basic Computer Vision\Contour.jpg",img)

cv2.waitKey(0)
    
  
cv2.destroyAllWindows()    