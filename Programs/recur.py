def prime(n,k):
    if(n<2):
        return False
    if(k==n):
        return True
    if(n%k==0):
        return False
    return prime(n,k+1)