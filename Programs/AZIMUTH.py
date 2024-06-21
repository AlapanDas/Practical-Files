def post():
    n=int(input("ENTER IMEI NUMBER"))
    l=len(str(n))
    cop=n
    for i in range(0,l):
        d=n%10
        n/=10
        if (i%2!=0):
            x=d*2