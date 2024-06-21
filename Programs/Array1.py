L=[]
L=eval(input("Input something"))
i=0
low=9
high=0
for i in range(0,len(L)):
    if L[i]>high:
        high=L[i]
    if L[i]<low:
        low=L[i]

print(high)
print(low)

