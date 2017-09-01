import random
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import uniform

N=int(input("enter the number of elements -(2 PARAMETERS(x,y) allowed FOR NOW)"))
K=N
x=[]
y=[]
M=[]
distance=np.zeros(shape=(N,N))
node=[]
for i in range(0,N):
    node.append(input("enter name of node -"));
    x.append(float(input("Enter the X coordinate of "+node[i]+"-")))
    y.append(float(input("Enter the Y coordinate of "+node[i]+"-")))
print(node)
print(x)
print(y)

#M=np.matrix([x,y])
#print(M)

def euclidian_dist1(x1,y1,x2,y2):
    t=(x1-x2)**2
    u=(y1-y2)**2 
    dist= (round(t,2)+round(u,2))**0.5
    return dist
k=K
while k>2:
    min_v=999
    min_x=""
    min_y=""
    X_x=0
    Y_y=0
    for i in range(0,N):
        a=[]
        for j in range(0,N):
            if k==K:
                d=euclidian_dist1(x[i],y[i],x[j],y[j])
            else:
                d=distance[i][j]
            a.append(round(d,2))
            if i!=j:
                if d<=min_v:
                    min_v=d
                    min_x=node[i]
                    min_y=node[j]
                    X_x=i
                    Y_y=j
        distance[i]=a
    print(distance)
    print(min_x,min_y,X_x,Y_y)
    print(min_v)
    for j in range(0,N):
        if j==X_x or j==Y_y:
            node[Y_y]=min_x+","+min_y
            continue
        if distance[X_x][j]>=distance[Y_y][j]:
            distance[Y_y][j]=distance[Y_y][j]
            distance[j][Y_y]=distance[Y_y][j]
        else:
            distance[Y_y][j]=distance[X_x][j];
            distance[j][Y_y]=distance[X_x][j]
    distance=np.delete(distance, (X_x), axis=0)
    distance=np.delete(distance, (X_x), axis=1)
    print(distance)
    node.remove(node[X_x])
    x.remove
    N=N-1
    k=N
    print(node)
    print("\n\n")
        





    
