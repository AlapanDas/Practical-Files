def isprime(n):
    sum=0
    for i in range(2,n+1):
        if i%n==0:
            sum+=1
        if sum==1:
            return True
        else:
            return False
def isAdam(n):
    rev=0
    copy=n
    while n!=0:
        d=n%10
        rev=rev*10+d
        n=n//10
    l=str(rev**2).split()
    l2=str(copy**2).split()
    if l[::-1]==l2:
        return True
    else:
        return False

if __name__ == "__main__":
    n=int(input("Enter the Number"))
    if isprime(n) and isAdam(n):
        print("CONDITION MACTHED")
    else:
        print("CONDITION FAILED")
def bank():
    #ISC2010
    n=int(input("Enter Number"))
    l=["zero","one","two","three",""]


