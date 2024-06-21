from os import name
def kaprekar(num):
    copy=str(num)
    count=len(copy)
    sqnum=num**2
    left=sqnum//(10**count)
    right=sqnum%(10**count)
    if left+right==num:
        return True
    else:
        return False
if __name__ == "__main__":
    p=int(input("Enter limit"))  
    q=int(input("Enter limit"))
    freq=0
    for i in range(p,q+1):
        if kaprekar(i)==True:
            print(i)
            freq+=1
        else:
            pass
    print("FREQUENCY =",freq)