import random
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import uniform


a=[]
a1=[]
a2=[]
x=[]
w=[]

#system
N=int(input("Enter the length of variables in system-"))
for i in range(0,N):
    a1.append(float(input("Enter variable value "+str(i+1)+"->")))
    
#model
for i in range(0,N):
    a2.append(0.0)
    x.append(0.0)
    w.append(0.0)


#LMS
def LMS_func(w1,x,e):
    w2=w1+(2*0.4*x*e)
    return w2

i=0

while True:
    y=0.0
    y1=0.0

    #generating input serially
    a.append(round((random.uniform(0.0,1.0))-0.5,3))
    
    #shifting the values
    for j in range(0,N):
        if j==N-1:
            x[N-j-1]=a[i]
        else:
            x[N-j-1]=x[N-j-2]
            
    #calculating y and y1     
    for k in range(0,N):
        y=y+(a1[k]*x[k])
        y1=y1+(w[k]*x[k])
        
    #error calculation
    e=y-y1

    #LMS algorithm to update weights
    for l in range(0,N):
        w[l]=round(LMS_func(w[l],x[l],e),3)

    #checking the error value
    if -0.001< e <0.001 :
        break;

    #incrementing the input array size
    i=i+1
    
print("system-->",a1)
print("Model-->",w)
    

    
