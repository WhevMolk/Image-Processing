# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 22:48:30 2018

@author: Manuel
"""

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
import cv2
import glob
import os



images = [cv2.imread(file, cv2.IMREAD_UNCHANGED) for file in glob.glob("../data/A2/data/test1/*.png")]
file_names = os.listdir("../data/A2/data/test1/")

model = VGG16()

for img, name in zip(images, file_names):    
    # load the model
   
    # load an image from file
    #image = load_img(img, target_size=(224, 224))
    # convert the image pixels to a numpy array
    image = cv2.resize(img, (224,224))
    #image = img_to_array(img)
    # reshape data for the model
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    # prepare the image for the VGG model
    image = preprocess_input(image)
    # predict the probability across all output classes
    yhat = model.predict(image)
    # convert the probabilities to class labels
    label = decode_predictions(yhat)
    # retrieve the most likely result, e.g. highest probability
    label1 = label[0][0]
    label2 = label[0][1]
    # print the classification
    print('%s %s (%.2f%%)' % (name,label1[1], label1[2]*100))
    print('%s %s (%.2f%%)' % (name,label2[1], label2[2]*100))