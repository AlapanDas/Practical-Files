t=0

def trnsform(S,k):
    s=list(S)
    copy=s
    # f=0
    flag=0
    l=len(s)//2
    for i in range(l):
        if s[l-i] != s[l+i]:
            if k>=1:                
                k-=1
            else:
                break   
        else:
            if k<=0:
                break
            else:
                pass    
    if s[::-1]==copy:
        return True
    else:
        return False
        


try:
    t=int(input())
except:
    pass
for i in range(t):
    n,k= map(int,input().split())
    s=input()
    if (trnsform(s,k)==True):
        print("YES")
    else:
        print("NO")



