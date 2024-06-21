t=0
n=[]
case=0
try:
     t=int(input())
except:
     pass
for i in range(t):
    n=eval((input()))
    #checking for G.P and A.P
    a=n[0]
    b=n[1]
    c=n[2]
    if a==0:
        break
    r=a/b
    d=b-a
    if r*(1/r)==c:
        case=1
    elif d+b==c:
        case=2
    if case==1:
        print(c*(1/r))
    elif case==2:
        print(c+d)
    else:
        pass