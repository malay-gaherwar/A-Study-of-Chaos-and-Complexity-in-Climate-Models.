# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 10:29:58 2020

@author: gaherwar
"""


def f(x,y):
    return r*x*(1-x)+c*y

def g(x,y):
    return c*(x+y)
import matplotlib.pyplot as plt
import math
import numpy as np
"""
Derivatives:
    f/x=r-2rx
    f/y=c
    g/x=c
    g/y=c   
"""
n=1
r=3.80
x=0.51
y=0.77
c=0.05
while(c<=0.1):
    lce=np.ones(200)
    q=np.array([[1,0],[0,1]])

    for i in range(1,160):
        u=x
        M=np.array([[r-2*r*x,c],[c,c]])
        q=np.dot(M,q)
        #print(q)
        #print(u)
        values , vectors = np.linalg.eig(q)
       # print("                    ")
        #print (values)
        #print(vectors)
        #print(max(abs(values))**(1/i))
        ab1=math.sqrt(values[0].real**2 + values[0].imag**2)
        ab2=math.sqrt(values[1].real**2 + values[1].imag**2)
        #print(max(ab1,ab2))
        lce[i]=math.log((max(ab1,ab2))**(1/i))
        #print(lce[i])
        x= f(x,y)
        y=g(u,y)
         


    z=np.linspace(1,21,20)
#print(lce)
#lce1=lce[99:159]
#print(len(lce1))

    plt.plot(z,lce[1:21])
    plt.xlabel("n")
    plt.ylabel("lce")
    plt.grid(True)
    plt.legend(('c= 0.05','c= 0.06','c= 0.07','c= 0.08','c= 0.09','c= 0.10'))
    plt.show
    c+=0.01




























"""import math
import numpy as np
from numpy.linalg import eig
n=1
r=3.7
x=2
c=0.05

a=np.array([[r*(1 - 2*x),c],[c,c]])   
values , vectors = eig(a)
print(values)
#print(vectors)

lce=math.log(max(abs(values))**(1/n))
print(lce)


"""





"""
from math import log
 
def d(series,i,j):
    return abs(series[i]-series[j])
 

series=[0.01,0.0122,0.0164,0.024,0.0453,0.0566,0.0664]

N=len(series)
eps=0.018
dlist=[[] for i in range(N)]
n=0 #number of nearby pairs found
for i in range(N):
    for j in range(i+1,N):
        if d(series,i,j) < eps:
            n+=1
            print (n)
            for k in range(min(N-i,N-j)):
                dlist[k].append(log(d(series,i+k,j+k)))

for i in range(len(dlist)):
    if len(dlist[i]):
        print ( i, sum(dlist[i])/len(dlist[i]))
"""