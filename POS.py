import math
import numpy as np
import random
position=[]
velocity=[]
pbest=[]

vmag=[]
w0=0.9
w1=0.4
c1=2
c2=2
#population size
NP=50
H={}
count=0
f=int(input("Enter 1-sinx, 2->cosx"))


def Eval_Func(x):
    if f==1:
        return math.sin(x)
    elif f==2:
        return math.cos(x)


#initializing position and velocity vecotor
for i in range(0,NP):
    a=[]
    b=[]
    a.append(Eval_Func(round(random.uniform(0.0,(2*math.pi)),3)))
    a.append(Eval_Func(round(random.uniform(0.0,(2*math.pi)),3)))
    b.append((random.uniform(0,1)-0.5))
    b.append((random.uniform(0,1)-0.5))
    position.append(a)
    velocity.append(b)
    pbest.append(a)
for i in range(0,NP):
    print(position[i])
#print(pbest)
while count<700:
    count=count+1
    for i in range(0,NP):
        v=(((pbest[i][0])**2)+((pbest[i][1])**2))**(0.5)
        H[v]=i
        vmag.append(v)
    vmag.sort()
    gbest=[]
    gbest.append(position[H[vmag[NP-1]]])
    
    #print(gbest)
    for i in range(0,NP):
        w=(w0)-((w0-w1)*(count-1))/699
        p1=(((position[i][0])**2)+((position[i][1])**2))**(0.5)
        #print(p1)
        velocity[i][0]=w*velocity[i][0]+(c1*(random.uniform(0,1)-0.5)*(pbest[i][0]-position[i][0])) + (c2*(random.uniform(0,1)-0.5)*(gbest[0][0]-position[i][0]))
        if velocity[i][0]>0.5:
            velocity[i][0]=0.49
        elif velocity[i][0]<(-0.5):
            velocity[i][0]=(-0.49)
        velocity[i][1]=w*velocity[i][1]+(c1*(random.uniform(0,1)-0.5)*(pbest[i][1]-position[i][1])) + (c2*(random.uniform(0,1)-0.5)*(gbest[0][1]-position[i][1]))
        if velocity[i][1]>0.5:
            velocity[i][1]=0.49
        elif velocity[i][1]<(-0.5):
            velocity[i][1]=(-0.49)
        p=(((position[i][0])**2)+((position[i][1])**2))**(0.5)
        #print(velocity[i])
        
        position[i][0]=position[i][0]+velocity[i][0]
        if(position[i][0]>=1.0):
            position[i][0]=0.999
        elif position[i][0]<=(-1.0):
            position[i][0]=(-0.999)
        position[i][1]=position[i][1]+velocity[i][1]
        if(position[i][1]>=1.0):
            position[i][1]=0.999
        elif position[i][1]<=(-1.0):
            position[i][1]=(-0.999)
        if p>p1:
            pbest[i]=position[i]
        #print("\n",position[i])
if f==1: 
    print("Maximizing-sinx")
else:
    print("Maximizing-cosx")
print("gbest-->",gbest)





