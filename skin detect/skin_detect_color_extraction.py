# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 17:27:58 2018

@author: Manuel

skin detection with color range extraction from given ground truth images
"""


import cv2
import glob
import numpy as np
import os


images = [cv2.imread(file, cv2.IMREAD_UNCHANGED) for file in glob.glob("../data/A1/data/extraction/train/*.png")]
masks = [cv2.imread(file, cv2.IMREAD_UNCHANGED) for file in glob.glob("../data/A1/data/extraction/mask/*.png")]

data_train = []
target_train = []
   
lower_B = 255
lower_G = 255
lower_R = 255

upper_B = 0
upper_G = 0
upper_R = 0
 


for img,mask in zip(images, masks): 
    for i in range(0, img.shape[0]):
         for j in range(0, img.shape[1] ):   
             if(mask[i][j][0] == 255):
                 if (img[i][j][0] < lower_B) : lower_B = img[i][j][0]
                 if (img[i][j][1] < lower_G) : lower_G = img[i][j][1]
                 if (img[i][j][2] < lower_R) : lower_R = img[i][j][2]
                 
                 if (img[i][j][0] > upper_B) : upper_B = img[i][j][0]
                 if (img[i][j][1] > upper_G) : upper_G = img[i][j][1]
                 if (img[i][j][2] > upper_R) : upper_R = img[i][j][2]
                 
    #print("Lower range: [" + str(lower_B) + "," + str(lower_G) + "," + str(lower_R) + "]")
    #print("Upper range: [" + str(upper_B) + "," + str(upper_G) + "," + str(upper_R) + "]")

print("Lower range: [" + str(lower_B) + "," + str(lower_G) + "," + str(lower_R) + "]")
print("Upper range: [" + str(upper_B) + "," + str(upper_G) + "," + str(upper_R) + "]") 

lower = np.array([lower_B, lower_G, lower_R], dtype = "uint8")
upper = np.array([upper_B, upper_G, upper_R], dtype = "uint8")

images = [cv2.imread(file, cv2.IMREAD_UNCHANGED) for file in glob.glob("../data/A1/data/extraction/test/*.png")]
file_names = os.listdir("../data/A1/data/extraction/test/")

for img,name in zip(images,file_names):  
    skinMask = cv2.inRange(img, lower, upper)
    skin = cv2.bitwise_and(img, img, mask = skinMask)
    
    cv2.imwrite("../data/A1/data/extraction/out/out-" + name,skinMask)
             
