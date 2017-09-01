import random
import math
import pandas as pd
import matplotlib.pyplot as plt
 from random import uniform

x=[]
fx=[]
p=[]
D={}
N=int(input())
V=1

Pc=0.8
u=20

Pm=0.2
n=20

CL=int(math.ceil(Pc*N))
ML=int(math.ceil(Pm*2.0*CL*V))
print(ML)

f=int(input("Enter 1-sinx, 2->cosx , 3->sinx +cosx"))


def Eval_Func(x):
    if f==1:
        return math.sin(x)
    elif f==2:
        return math.cos(x)
    elif f==3:
        return math.sin(x) + math.cos(x)


def tournament_selection(x,y):
    if(fx[x]<=fx[y]):
        return x
    else:
        return y

def crossover(x,y):
    r=random.uniform(0.0,1.0)
    if(r<=0.5):
        b=(2*r)**(1/(u+1))
    else:
        b=(1/(2*(1-r)))**(1/(u+1))
    c1=round((1/2)*(((1+b)*p[x])+((1-b)*p[y])),3)
    c2=round((1/2)*(((1-b)*p[x])+((1+b)*p[y])),3)
    return c1,c2
def mutation(x):
    r=random.uniform(0.0,1.0)
    if(r<=0.5):
        d=((2*r)**(1/(n+1)))-1
    else:
        d=1-((2*(1-r))**(1/(n+1)))
    m=round(C[x]+d,3)
    return m
    
num=[]    
for i in range(N):
    num.append(i)
count=0
for i in range(N):
            x.append(round(random.uniform(0.0,(2*math.pi)),3))
            v=Eval_Func(x[i])
            fx.append(round(v,3))
plt.scatter(x,fx)
plt.show()
#fig, ax = plt.subplots()
#ax.scatter(x,fx)
#DF=pd.DataFrame({'x':x,'y':fx})
#RandIndex=random.randint(0,len(DF),size=20)
#DF.iloc[RandIndex].plot(x='x',fx='y',kind='scatter',s=120,ax=plt.gca())
while count<=1000:
        count=count+1
        C=[]
        M=[]
        R=[]
        S=[]
        for i in range(N):
            fx.append(round(Eval_Func(x[i]),3))
        #print("Initialize Population(X)--->",x,"\n\nEvaluate Function(Fx)-->",fx)
        #print("\n\n")

        for i in range(N):
            st=tournament_selection(random.randint(0,9),random.randint(0,9))
            p.append(x[st])
        #print("Tournament Selection(P)--->",p)
        #print("\n\n")

        for i in range(CL):
            c1,c2=crossover(random.randint(0,9),random.randint(0,9))
            C.append(c1)
            C.append(c2)
        #print("Crossover(C)--->",C)
        #print("\n\n")

        for i in range(ML):
            m=mutation(random.randint(0,15))
            M.append(m)
        #print("Mutation(M)--->",M)
        #print("\n\n")
        fx=[]
        t=0
        for i in range(len(x)):
            R.append(x[i])
            fx.append(round(Eval_Func(x[i]),3))
            D[fx[t]]=x[i]
            t=t+1
        for i in range(len(C)):
            R.append(C[i])
            fx.append(round(Eval_Func(C[i]),3))
            D[fx[t]]=C[i]
            t=t+1
        for i in range(len(M)):
            R.append(M[i])
            fx.append(round(Eval_Func(M[i]),3))
            D[fx[t]]=M[i]
            t=t+1
            
        #print("(X+C+M)->(R)--->",R)
        #print("\n\n")
        fx.sort()
        #print("Sorted fx--->",fx)



        for i in range(N):
            S.append(fx[i])
        #print("Selected fx--->",S)    
        SR=[]
        CR=[]
        for i in range(N):
            CR.append(fx[i])
            SR.append(D[fx[i]])
        x=SR
        fx=[]

plt.scatter(SR,CR)
plt.show()



    
print("\n\nSelection of N chromosomes for Next Generation--->",SR)
    
               
    
    

