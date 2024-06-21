n=int(input("Enter test cases"))
L=[]
for i in range(n):
    no , bud  = map(int,(input().split()))
    L= list(map(int,input().split()))
    sum=0
    for j in range(len(L)):
        sum=sum+L[j]
    if sum>1000:
        sum=sum-sum*0.1
    if sum>bud:
        print("NO")
    if sum<=bud:
        print("YES")

