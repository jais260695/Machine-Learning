from sklearn.datasets import load_iris
import random
from random import uniform
iris=load_iris()


def euclidian_dist1(sl,sw,pl,pw):
    dist= ( ((sl-c1[0])**2)+((sw-c1[1])**2)+((pl-c1[2])**2)+((pw-c1[3])**2))**0.5
    return dist
def euclidian_dist2(sl,sw,pl,pw):
    dist= ( ((sl-c2[0])**2)+((sw-c2[1])**2)+((pl-c2[2])**2)+((pw-c2[3])**2))**0.5
    return dist

def euclidian_dist3(sl,sw,pl,pw):
    dist= ( ((sl-c3[0])**2)+((sw-c3[1])**2)+((pl-c3[2])**2)+((pw-c3[3])**2))**0.5
    return dist

def minimum_dist(dist_c1,dist_c2,dist_c3):
    if(dist_c1 <= dist_c2 and dist_c1 <=dist_c3):
        return 0
    elif(dist_c2 <= dist_c3):
        return 1
    else:
        return 2



r1=random.uniform(0.0,1.0)
r2=random.uniform(0.0,1.0)
r3=random.uniform(0.0,1.0)

c1=iris.data[(int)(r1*149)]
c2=iris.data[(int)(r2*149)]
c3=iris.data[(int)(r3*149)]

cluster1=[]
cluster2=[]
cluster3=[]
check1=[-1]
check2=[-1]
check3=[-1]

t1=0
t2=0
t3=0

count=0
while ((check1!=cluster1) or (check2!=cluster2) or (check3!=cluster3)):
    
    count=count+1
    t1=0
    t2=0
    t3=0
    check1=cluster1
    check2=cluster2
    check3=cluster3
    cluster1=[]
    cluster2=[]
    cluster3=[]

    for i in range(len(iris.target)):        
        c=iris.data[i]
        dist_c1=euclidian_dist1(c[0],c[1],c[2],c[3])
        dist_c2=euclidian_dist2(c[0],c[1],c[2],c[3])
        dist_c3=euclidian_dist3(c[0],c[1],c[2],c[3])
        min_dist=minimum_dist(dist_c1,dist_c2,dist_c3)
        if(min_dist==0):  
            cluster1.append(i)
            t1=t1+1
        elif(min_dist==1):
            cluster2.append(i)
            t2=t2+1
        else:
            cluster3.append(i)
            t3=t3+1
    sl=0.0
    sw=0.0
    pl=0.0
    pw=0.0
    for j in range(t1):
          sl=sl+iris.data[cluster1[j]][0]
          sw=sw+iris.data[cluster1[j]][1]
          pl=pl+iris.data[cluster1[j]][2]
          pw=pw+iris.data[cluster1[j]][3]
    try:
       c1[0]=sl/t1
       c1[1]=sw/t1
       c1[2]=pl/t1
       c1[3]=pw/t1
    except ZeroDivisionError as detail:
       print ('Handling run-time error:', detail)
    

    sl=0.0
    sw=0.0
    pl=0.0
    pw=0.0
    for k in range(t2):
        sl=sl+iris.data[cluster2[k]][0]
        sw=sw+iris.data[cluster2[k]][1]
        pl=pl+iris.data[cluster2[k]][2]
        pw=pw+iris.data[cluster2[k]][3]
    try:
       c2[0]=sl/t2
       c2[1]=sw/t2
       c2[2]=pl/t2
       c2[3]=pw/t2
    except ZeroDivisionError as detail:
       print ('Handling run-time error:', detail)
    
    
    sl=0.0
    sw=0.0
    pl=0.0
    pw=0.0
    for l in range(t3):
        sl=sl+iris.data[cluster3[l]][0]
        sw=sw+iris.data[cluster3[l]][1]
        pl=pl+iris.data[cluster3[l]][2]
        pw=pw+iris.data[cluster3[l]][3]

    try:
       c3[0]=sl/t3
       c3[1]=sw/t3
       c3[2]=pl/t3
       c3[3]=pw/t3
    except ZeroDivisionError as detail:
       print ('Handling run-time error:', detail)
    
   

print(t1)
print(t2)
print(t3)

print(cluster1)
print(cluster2)
print(cluster3)

print(count)


