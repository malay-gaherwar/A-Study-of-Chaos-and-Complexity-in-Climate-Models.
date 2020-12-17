# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 19:07:06 2020

@author: gaherwar
"""
import matplotlib.pyplot as plt
#import math
import numpy as np
#from numpy.linalg import eig
x=np.ones(200)
y=np.ones(200)
x[0]=0.51
y[0]=0.61
r=3.7
c=0.09

for n in range(1,200):
    x[n]=r*x[n-1]*(1-x[n-1]) +c*y[n-1]
    y[n]=c*(x[n-1] + y[n-1])
    

t=np.linspace(1,200,200)

plt.scatter(t,x,s=5)
plt.scatter(t,y,s=5,c='red')
plt.xlabel("time")
plt.ylabel("Values of x and y")
plt.legend(['x values','y values'],loc="upper right")
plt.show
 