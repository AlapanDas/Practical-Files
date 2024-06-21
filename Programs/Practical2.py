n=int(input("Enter n"))
a=(input("Enter 1st Char"))
b=(input("Enter 1st Char"))
c=(input("Enter 1st Char"))
l=[[0 for x in range(n) for y in range(n)]]
l[0][0]=l[0][n-1]=l[n-1][0]=l[n-1][n-1]=a
for i in range(n):
    for j in range(n):
        if (i,j) in [0,n-1]:
            l[i][j]=b
        else:
            l[i][j]=c
print(l)
def alternate():
    n= int(input())
    a=(input("Enter 1st Char"))
    b=(input("Enter 1st Char"))
    c=(input("Enter 1st Char"))
    if n<3 and n>10:
        print("INVALID!")
    else:
        L=[]
        L.append(a+b*(n-2)+a)
        for a in range(1,n-1):
            L.append(b+c*(n-2)+b)
        L.append(a+b*(n-1)+a)