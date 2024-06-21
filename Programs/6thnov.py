n=int(input("Enter n"))
if n>2 and n<10:
    pass
else:
    exit
l=eval(input("input 1d list"))
l.sort()
L=[]
L.append(l)
for i in range(len(l)):
    x=l[:len(l)-1]+l[:i]
    L.append(x)
for i in L:
    print(i)
