from decimal import DivisionByZero
from sympy import true


def iscollinear(l1,l2,l3):
    try:
        slope1=(l2[1]-l1[1])/(l2[0]-l1[0])
    except ZeroDivisionError:
        slope1=0
    try:
        slope2=(l3[1]-l2[1])/(l3[0]-l2[0])
    except ZeroDivisionError:
        slope2=0
    if(slope1==slope2):
        return True
    else:
        return False
def isantipodal(l1,l2,l3):
    try:
        slope1=(l2[1]-l3[1])/(l2[0]-l3[0])
    except ZeroDivisionError:
        slope1=0
    try:
        slope2=(l1[1]-l2[1])/(l1[0]-l2[0])
    except ZeroDivisionError:
        slope2=0
    if(slope1*slope2==-1):
        return True
    else:
        return False

try:
    t=int(input())
except:
    pass
for i in range(t):
    n=int(input())
    l=[]
    L=[]
    for i in range(n):
        x,y=map(int,input().split())
        l.append([x,y])
    for i in range(n):
        for j in range(i,n):
            for k in range(j,n):
                if(iscollinear(l[i],l[j],l[k])==True):
                    if(isantipodal(l[i],l[j],l[k])):
                        L.append([i,j])
                    if(isantipodal(l[j],l[k],l[i])):
                        L.append([j,k])
                    else:
                        L.append([i,k])
    
    count=0
    for a in L: 
        n = L.count(a)
        if n > 1:
            if L.count(a) >1:
                count+=1
    print(count)