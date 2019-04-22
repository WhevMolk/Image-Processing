# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 11:51:19 2018

@author: Manuel

Implementation of threshold based skind detection

Threshold parameters are taken from: Kolkur, S., Kalbande, D., Shimpi, P., Bapat, C., Jatakia, J., 2016.
 Human Skin Detection Using RGB, HSV and YCbCr Color Models. Roeper Review. doi:10.2991/iccasp-16.2017.51
"""

import cv2
import numpy as np
from PIL import Image
import glob
import os
import sys

images = [cv2.imread(file, cv2.IMREAD_UNCHANGED) for file in glob.glob("../data/test/*.png")]
file_names = os.listdir("../data/test/")


#R > 95 and G > 40 and B > 20 and R > G and R > B and | R - G | > 15 and
# A > 15 and Cr > 135 and Cb > 85 and Y > 80 and Cr <= (1.5862*Cb)+20 
#and Cr>=(0.3448*Cb)+76.2069 and Cr >= (-4.5652*Cb)+234.5652 
#and Cr <= (-1.15*Cb)+301.75 and Cr <= (-2.2857*Cb)+432.85

for img, name in zip(images, file_names):    

    for i in range(0, img.shape[0]):
         for j in range(0, img.shape[1] ):   
             B = img[i][j][0]
             G = img[i][j][1]
             R = img[i][j][2]
             
    # how to convert from RGB to YCrCb
    # https://docs.opencv.org/3.4.3/de/d25/imgproc_color_conversions.html         
            # Y = 0.299 * R + 0.587 * G + 0.114 *B
            # Cr = (R - Y) * 0.713 + 128
            # Cb = (B - Y) * 0.564 + 128
             
             # there is no alpha value in our png images
             if ((R > 95) 
                 and (G > 40) 
                 and (B > 20) 
                 and (R > G) 
                 and (R > B) 
                 and (abs(R - G) > 15) ):
                 
                 #the results with my test sets often were better without threshold for YCrCb
                 #and Y > 80 
                 #and Cr <= (1.5862*Cb)+20 
                 #and Cr>=(0.3448*Cb)+76.2069 
                 #and Cr >= (-4.5652*Cb)+234.5652 
                 #and Cr <= (-1.15*Cb)+301.75 
                 #and Cr <= (-2.2857*Cb)+432.85):
                    img[i][j] = [255,255,255]
                    
             else:
                img[i][j] = [0,0,0]
               
    #opening (erosion -> dilation)
    kernel = np.ones((5,5),np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
               
    cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("../data/out/out-" + name + ".png",img)
   
             
             

  
    

