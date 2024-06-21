def push(data,l):
    if(top==len(l)-1):
        print("Overflow")
    else:
        l.append(data)
def pop():
    if (top==0):
        print("Underflow")
    else:
        l.pop()
def peek():
    print(top) 
l=[1,2,3,4]
top=-1
push(5,l)
pop()
print(l)