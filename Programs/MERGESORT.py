def take(a,b):
    l=a+b
    l.sort()
    return l

if __name__ == "__main__":
    a=eval(input("ENTER 1ST LIST"))
    b=eval(input("ENTER 2ND LIST"))
    print(take(a,b))