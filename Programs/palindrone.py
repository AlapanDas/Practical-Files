def sillystring():
    s=input("enter the string")
    l=[]
    for i in range(len(s)):
        key=s[i]
        k=1
        while True:
            f=s.find(key,k)
            if f==-1:
                break
            ch=s[i:f+1]
            if checkforpalindrome(ch)==1:
                l.append(ch)
            k+=1
    l.sort()
    print(l[-1])

def checkforpalindrome(x):
    if x[::-1]==x:
        return 1
    else:
        return -1
 
sillystring()
