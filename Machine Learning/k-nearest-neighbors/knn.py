# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 19:08:16 2018

@author: Manuel Olk
"""

#Load libraries
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


#create dataset

xs = [1.1, 0.7, 1.3, 1.8, 1, 0.9, 1.5, 1.2, 1.4, 1.3, 1.5, 5, 2.4, 2, 2, 2.1, 2.2, 2.5, 2.3, 2.8, 3.1, 3.2, 2.9]
ys = [1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2, 4, 4.1, 4.2, 4.3, 4.4, 4.5, 4.7, 4.8, 4, 4.2, 4.1]

data = [xs, ys]

#data = pd.DataFrame(dataset, columns = ['x','y'])
df1 = pd.DataFrame({'x' : xs})
df2 = pd.DataFrame({'y' : ys})

#dataset = pd.concat([df1,df2], axis =1)
dataset = df1.join(df2)
        
dataset.plot(kind = 'scatter', x = 'x', y='y')
print(dataset)

# implementation of the algorithm

