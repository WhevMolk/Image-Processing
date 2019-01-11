# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 20:15:23 2018

@author: Manuel

Person detection with haarcascade
"""

import cv2
import os
import glob

casc_body_path = "haarcascade_fullbody.xml"

images = [cv2.imread(file, cv2.IMREAD_UNCHANGED) for file in glob.glob("../data/A2/data/test/*.png")]
file_names = os.listdir("../data/A2/data/test/")

casc_body_path = cv2.CascadeClassifier(casc_body_path)

with open("../data/A2/data/result.txt", 'w') as res:
    

    for img, name in zip(images, file_names):    

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        persons = casc_body_path.detectMultiScale(gray)
        # Draw a rectangle around the person
        
        if len(persons) == 0:
            res.write("0\n")
        else:
            res.write("1\n")
            
        #for (x, y, w, h) in persons:
        #    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0 ), 2)
            
        
            
        #cv2.imwrite("../data/A2/data/out/out-" + name,img)
                
                