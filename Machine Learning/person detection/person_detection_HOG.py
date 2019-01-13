# -*- coding: utf-8 -*-
"""
Created on Fri Jan 1 13:15:23 2019

@author: Manuel

Person detection with HOG
"""

import cv2
import os
import glob

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

images = [cv2.imread(file, cv2.IMREAD_UNCHANGED) for file in glob.glob("../data/A2/data/test/*.png")]
file_names = os.listdir("../data/A2/data/test/")



with open("../data/A2/data/result.txt", 'w') as res:
    

    for img, name in zip(images, file_names):    

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        (rects, weights) = hog.detectMultiScale(gray,winStride=(1, 1),
        padding=(4, 4), scale=1.005)
        # Draw a rectangle around the faces
        
       
        if len(rects) == 0:
            res.write("0\n")
        else:
            res.write("1\n")
            
        #for (x, y, w, h) in rects:
        #    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0 ), 2)
            
        
            
        #cv2.imwrite("../data/A2/data/out/out-" + name,img)
                
                