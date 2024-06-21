l=[]
l=eval(input())
obj=int(input("Enter a number to search in the array"))
i=0
pos=0
for i in range(0,len(l)):
    if l[i]==obj:
        pos=i
        break
print(pos+1)
