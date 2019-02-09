# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 17:27:58 2019

@author: Manuel


Calculates the string length distribution of the ORAND datasets

http://www.orand.cl/en/icfhr2014-hdsr/#datasets
"""



import csv
import os
import glob


txt_files = glob.glob("*.txt")

for txt in txt_files:
    list = [0,0,0,0,0,0,0,0,0,0]
    with open(txt, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        for row in csv_reader:
            
            #print(f'{" ".join(row)}')
            length = len(" ".join(row)) - 17
            list[length] = list[length] + 1
        
        print('b_test_gt.txt')
        print(list)
       