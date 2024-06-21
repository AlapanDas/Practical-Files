import copy
t=0
try:
    t=int(input())
except:
     pass
for i in range(t):
    n=int(input())
    l=list(input().split(' '))
    slist=l[:]
    slist.sort()
    for j in range(len(l)):
        key = j
        for k in range(j+1,len(l)):
            if l[k]< l[key] and (j+1 & k+1)!=0:
                key=k
            l[j], l[key] = l[key], l[j]

    if l==slist:
        print("yes")
    else:
        print("no")

