def fact(x):
    flag=1
    for i in range(1,x+1):
        flag=flag*i
    return flag
if __name__=='__main__':
    n=0
    r=0
    test=0
    try:
        test=int(input())
    except:
        pass
    for i in range(test):
        n , r  = map(int,(input().split()))
        ncr=fact(n)/(fact(n-r))
        print(ncr)
