# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 21:08:05 2018

@author: Manuel
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 21:31:01 2018
BGR to gray scale converter

@author: Manuel
"""

import cv2
import glob
import os


def convert():
    print("Starting preprocessing..")
    images = [cv2.imread(file, cv2.IMREAD_UNCHANGED) for file in glob.glob("C:/Users/Manuel/Desktop/GIT/NN_Praktikum/digit-string-recognition/ORAND-CAR-2014/CAR-A/a_test_images/*")]
    file_names = os.listdir("C:/Users/Manuel/Desktop/GIT/NN_Praktikum/digit-string-recognition/ORAND-CAR-2014/CAR-A/a_test_images/")
    
    for img, name in zip(images, file_names):    
       # ImageOps.autocontrast(img, cutoff=0, ignore=None)    
       
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


        
        cv2.imwrite("C:/Users/Manuel/Desktop/GIT/NN_Praktikum/digit-string-recognition/ORAND-CAR-2014/CAR-A/a_test_images_gray/"+ name,img)

if __name__ == "__main__":
    convert()
   