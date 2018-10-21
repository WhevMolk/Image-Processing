# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 22:02:21 2018

@author: Manuel Olk
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 19:08:16 2018

@author: Manuel Olk
"""

# load libraries
import pandas as pd
import random
import numpy as np
import math


def euklid(node, center):
    sum=0
    for i in range(2):
        sum+=math.pow(node[i]-center[i],2)
    return math.sqrt(sum)    

# create dataset
xs = [1.1, 0.7, 1.3, 1.8, 1, 0.9, 1.5, 1.2, 1.4, 1.3, 1.5, 5, 2.4, 2, 2, 2.1, 2.2, 2.5, 2.3, 2.8, 3.1, 3.2, 2.9]
ys = [1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2, 4, 4.1, 4.2, 4.3, 4.4, 4.5, 4.7, 4.8, 4, 4.2, 4.1]

data = [xs, ys]

# data = pd.DataFrame(dataset, columns = ['x','y'])
df1 = pd.DataFrame({'x' : xs})
df2 = pd.DataFrame({'y' : ys})


# dataset = pd.concat([df1,df2], axis =1)
dataset = df1.join(df2)
dataset['c'] = np.nan 
       

#print(dataset)

# implementation of the k-means algorithm
def kmeans(k, cluster_center, old_cluster_center):
    # first method call?
    # choose random start cluster center

    if (cluster_center == []):      
        print("first_call")
        for i in range (0, k):
            ran_x = random.randint(0,5)
            ran_y = random.randint(0,5)
            cluster_center.append([ran_x, ran_y, i])
    else:     
    # converged?
        sum_conv = 0
        for c in range(0, len(cluster_center)):
            print(old_cluster_center[c])
            print(cluster_center[c])
            sum_conv += euklid(old_cluster_center[c], cluster_center[c])
            print("conv " + str(sum_conv))
        if sum_conv <= 0.05:
            return
    
    # iterate over all nodes and colour them like the center closest to them
    for i in range(0, len(dataset.index)):
        closest_center = cluster_center[0]
        for c in cluster_center:   
            if (euklid([dataset['x'][i],dataset['y'][i]], c) < euklid([dataset['x'][i],dataset['y'][i]], closest_center)):
                closest_center = c 
        dataset['c'][i] = closest_center[2]
               

    # safe old center for convergence check
    old_cluster_center = cluster_center.copy()
   
    # calculate new center
    for c in range(0, len(cluster_center)):
        count = 1
        acc_x = 0
        acc_y = 0
        for i in range (len(dataset.index)):
            if(dataset['c'][i] == cluster_center[c][2]):
                acc_x += dataset['x'][i]
                acc_y += dataset['y'][i]
                count += 1
        cluster_center[c] = [acc_x / count, acc_y / count, cluster_center[c][2]]
    
  
    kmeans(k, cluster_center, old_cluster_center)

cluster_center = []
old_cluster_center = []
kmeans(2, cluster_center, old_cluster_center)
#print(dataset)
dataset.plot.scatter(x ='x', y='y', c='c', colormap = 'viridis')

