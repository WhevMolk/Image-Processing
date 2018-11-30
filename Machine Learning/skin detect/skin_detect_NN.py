# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 21:31:01 2018

@author: Manuel
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 19:03:50 2018
skin detection via k nearest neighbor
@author: Manuel
"""

import cv2
import glob
import numpy as np
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix 
from sklearn.svm import SVC
import pickle

#classifier = SVC(kernel='linear', C = 1.0)
classifier = KNeighborsClassifier(n_neighbors = 5)

def train():
    print("Starting training..")
    images_train = [cv2.imread(file, cv2.IMREAD_UNCHANGED) for file in glob.glob("../data/A1/data/train/img-1153828*.png")]
    masks_train = [cv2.imread(file, cv2.IMREAD_UNCHANGED) for file in glob.glob("../data/A1/data/train/mask-img-1153828*.png")]
    
    data_train = []
    target_train = []
    
    for img,mask in zip(images_train, masks_train): 
        for i in range(0, img.shape[0]):
             for j in range(0, img.shape[1] ):   
                 data_train.append(img[i][j])             
                 target_train.append(mask[i][j][0])
                   
    data_train = np.array(data_train)
    target_train = np.array(target_train)
    print(data_train.shape)     
    classifier.fit(data_train, target_train)


def safe_model():
    filename = 'finalized_model.sav'
    pickle.dump(classifier, open(filename, 'wb'))    

#def load_model():
#    filename = 'finalized_model.sav'
#    classifier = pickle.load(open(filename, 'rb'))     

  
def validate(): 
    print("Starting validation..")
    images_val = [cv2.imread(file, cv2.IMREAD_UNCHANGED) for file in glob.glob("../data/A1/data/validation/cond2-*.png")]
    masks_val = [cv2.imread(file, cv2.IMREAD_UNCHANGED) for file in glob.glob("../data/A1/data/validation/mask-cond2-*.png")]
    
   
    for img,mask in zip(images_val, masks_val): 
        data_val = []
        target_val = []
        for i in range(0, img.shape[0]):
             for j in range(0, img.shape[1] ):   
                 data_val.append(img[i][j])             
                 target_val.append(mask[i][j][0])
                   
    data_val = np.array(data_val)
    target_val = np.array(target_val)
    
    target_pred = classifier.predict(data_val)
    print(data_val.shape)
    print(data_val.head) 
    
    print(confusion_matrix(target_val, target_pred))  
    print(classification_report(target_val, target_pred))  
    
def classify():
    print("Starting classification..")
    images = [cv2.imread(file, cv2.IMREAD_UNCHANGED) for file in glob.glob("../data/A1/data/test/*.png")]
    file_names = os.listdir("../data/A1/data/test/")
    
    
    
    for img, name in zip(images, file_names):
        data = []
        target = []
        for i in range(0, img.shape[0]):
            for j in range(0, img.shape[1] ):   
                #img[i][j] = classifier.predict(img[i][j].reshape(1,-1))
                data.append(img[i][j])
        target = classifier.predict(data)
        
        for i in range(0, img.shape[0]):
           for j in range(0, img.shape[1] ): 
               img[i][j] = target[i*img.shape[1]+j] 
     #cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)
   
        cv2.imwrite("../data/A1/data/out/out-" + name,img)
 
    
def process():
    print("Starting postprocessing..")
    images = [cv2.imread(file, cv2.IMREAD_UNCHANGED) for file in glob.glob("../data/A1/data/out/*.png")]
    file_names = os.listdir("../data/A1/data/out/")
    
    
    for img, name in zip(images, file_names):    
        kernel = np.ones((5,5),np.uint8)
        img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
               
       
        cv2.imwrite("../data/A1/data/out_proc/" + name,img)

train()
classify()
process()
    

