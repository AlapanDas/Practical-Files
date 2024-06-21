from copy import copy
from random import randint
t=0
count=0
def check(arr):
    flag=1
    for i in range(len(arr)):
        if i+1 == int(arr[i]):
            flag*=1
            key=i
        else:
            flag*=-0
    if flag==1:
        # return that its A(i)=i
        return True
    else:
        # return that A(i) not = i 
        return False
try:
    t=int(input())
except:
    pass

for i in range(t):
    n=int(input())
    arr=list(input().split(' '))    
    k=randint(0,9)
    pos=randint(0,len(arr)-1)
    if check(arr)==True:
        print(count)
        break
    else:                
        while(check(arr)==True):   
            copy=arr
            k=randint(0,9)
            pos=randint(0,len(arr)-1)             
            copy.insert(pos,k)
            if check(copy)==False:
                count+=1
                print(count)
                break
            else:
                copy=0
                pass

    print(count)

