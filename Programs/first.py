L=[]
M=[]
#---------------------------
def unique(k):
    L.append(k)
def dup(o):
    M.append(o)
def max():
    max=0
    for i in M:
        if M.count(i)>=max:
            max=i
    print("highest frq=",max)
if __name__ == "__main__":
    lst=eval(input("ENTER 1ST LIST"))
    for i in lst:
        if lst.count(i)==1:
            unique(i)
        else:
            dup(i)  
    max()
    print("unique=",L)
    print("duplicate=",M)
#---------------------------