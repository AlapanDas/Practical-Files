n=int(input("Enter number of Test Cases"))
for i in range(n):
    a , b , c = map(int,(input().split(" ")))
    maximum_to_win=max(a,b,c)+1
    x=maximum_to_win-a
    y=maximum_to_win-b
    z=maximum_to_win-c
    if maximum_to_win-1==a:
        x=0
    if maximum_to_win-1==b:
        y=0
    if maximum_to_win-1==c:
        z=0
    print(int(x),"",int(y),"",int(z))