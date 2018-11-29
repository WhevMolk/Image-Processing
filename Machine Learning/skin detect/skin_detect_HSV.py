# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 19:03:50 2018
skin detection in HSV colour space
@author: Manuel
"""

import cv2
import numpy as np
import glob
import os

images = [cv2.imread(file, cv2.IMREAD_UNCHANGED) for file in glob.glob("../data/A1/data/test/*.png")]
file_names = os.listdir("../data/A1/data/test/")

# boundaries for skin color
lower = np.array([0, 48, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")


for img, name in zip(images, file_names):    
    conv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    skinMask = cv2.inRange(conv, lower, upper)
    
    
    # apply a series of erosions and dilations to the mask
	# using an elliptical kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    skinMask = cv2.erode(skinMask, kernel, iterations = 2)
    skinMask = cv2.dilate(skinMask, kernel, iterations = 2)
    
    # blur the mask to help remove noise
    skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
    # cv2.imwrite("../data/A1/data/maskBl/out-" + name,skinMask)
    
    # then apply the mask to the frame
    skin = cv2.bitwise_and(img, img, mask = skinMask)
    
               
    cv2.cvtColor(skin, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("../data/A1/data/out/out-" + name,skin)
   
             
             

  
    

