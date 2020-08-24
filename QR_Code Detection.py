# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 21:30:59 2020

@author: Abdelrahman
"""

import cv2 
from pyzbar.pyzbar import decode
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    
    _, frame = cap.read()
    
    im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, bw_im = cv2.threshold(im, 100, 255, cv2.THRESH_BINARY)
    
    for barcode in decode(bw_im):
        data = barcode.data.decode("utf-8")
        #pts = np.array([barcode.polygon],np.int32)
        #pts = pts.reshape((-1,1,2))
        #cv2.polygon(frame,[pts],True,(255,0,255),5)
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)
        cv2.putText(frame,data,(x,y),cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,(255,0,255),2)
        
    cv2.imshow("Barcode",frame)    
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
             break

cap.release()
cv2.destroyAllWindows()    
        
