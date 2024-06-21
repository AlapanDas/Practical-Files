def convert(num,base):
    n=0
    while num>0:
        d=int(num%base)
        n=n*10+d
        num//=base
    return n
##################################
if __name__ == "__main__":
    x=int(input("ENTER NUMBER"))
    y=int(input("ENTER BASE"))
    print(convert(x,y))

