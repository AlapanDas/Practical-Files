import copy


def check(arr):
    flag=0
    for i in arr:
        if int(i)&1==1:
            flag+=1
    if flag==len(arr):
        return True
    else:
        return False
    
for k in range(int(input())):
    n=int(input())
    a=list(input().split(' '))
    count=0
    for i in range(len(a)):
        for j in range(i,len(a)-1):
            copyy=copy.deepcopy(a)
            del copyy[i]
            del copyy[j]
            copyy.append(a[i]+a[j])
            if check(copyy)==True:
                count+=1
            else:
                pass
    print(count)