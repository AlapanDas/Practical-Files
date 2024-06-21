
t=0
money=0
def XOR(a):
    A=int(a[0])
    B=int(a[-1])
    oldkey= A^B
    for i in range(1,len(a)//2 +1,1):
        A=int(a[i-1])
        B=int(a[len(a)-1-i])
        if A^B == oldkey:
            flag=1
            oldkey=A^B
        else:
            flag=-1
    if flag==1:
        return True
    else:
        return False
    
try:
    t=int(input())
except:
    pass
for i in range(t):
    flag=-1
    l=int(input())
    s=input()
    ones=s.count('1')
    zeros=s.count('0')
    for i in range(len(s)//2):

        if (XOR(s)==True):
            flag=1
        else:
            flag=0
    if flag==1 or ones==zeros :
        print("YES")
    else:
        print("NO")