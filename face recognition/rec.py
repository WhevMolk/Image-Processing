# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 13:15:23 2019

@author: Manuel

Face recognition via face_recognition
data: folder with the public data set (853 pairs of faces 250x250px, eye-aligned) 


The goal is to train a classifier able to discern if two face images belong to the same person, or belong to different persons.
The main program uses a train and validation setup where half of the image pairs will belong to the same person and half will belong to different persons. 
First you should train your similitude measure, and then you will be asked to give a similitude value for several pairs of images. 
The score scale is not important, but must give larger values for pairs of faces belonging to the same person than for pairs of faces belonging to different persons. 

"""

import cv2
import os
import glob
import face_recognition as fr
import csv
import msvcrt as m
import numpy as np


#images = [cv2.imread(file, cv2.IMREAD_UNCHANGED) for file in glob.glob("../data/A2/data/test/*.png")]
#file_names = os.listdir("../data/A2/data/test/")




with open("../data/A3/data/testPairs.txt", 'r') as pairs, open("../data/A3/data/result.txt", 'w') as res:
    csv_reader = csv.reader(pairs, delimiter=' ')
    line_count = 0
    
    print("Starting...")
    counter = 0
    for row in csv_reader:

        print(row[0] + " || " + row[1])
        path1 = "../data/A3/data/test/" + row[0]
        path2 = "../data/A3/data/test/" + row[1]
        
        img1_load = fr.load_image_file(path1)
        img2_load = fr.load_image_file(path2)
        
        # when a face can not be found --> face_encodings == []
        if len(fr.face_encodings(img1_load)) == 0 or len(fr.face_encodings(img2_load)) == 0:
            result = [False]
        else:
            img1_encoded = fr.face_encodings(img1_load)[0]
            img2_encoded = fr.face_encodings(img2_load)[0]
       
            result = fr.compare_faces([img1_encoded], img2_encoded)
        
        print(result[0])
        if result[0]:
            res.write("1\n")
        else:
            res.write("0\n")
        '''
        img1 = cv2.imread(path1, 1)
        img2 = cv2.imread(path2, 1)
        stack = np.concatenate((img1, img2), axis = 1)
        
        
        cv2.imshow("Face", stack)
        char = cv2.waitKey(1000) & 0xFF
        if char == 27 or char == 113:
            print("exit")
            break
     
        cv2.destroyAllWindows()    
        '''
