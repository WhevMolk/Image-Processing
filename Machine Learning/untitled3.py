# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 20:29:07 2018

@author: Manuel Olk
"""

print("There are " + str(dataset.shape[0])+ " feature vectors of size " + str(dataset.shape[1]))

print(dataset.head(5))
print(dataset.describe())

#for our algorithm we only want two features
reduced_dataset = dataset.drop(['petal-length', 'petal-width'], axis = 1)

print(reduced_dataset.head(5))
print(reduced_dataset.describe())
