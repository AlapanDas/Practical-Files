n=int(input("Enter the number"))
l=len.n  
copy=n
for i in range (l):
     d=n%10
     n=n/10
     sum+=d**3
if sum==copy:
     print("Armstrong Number")

