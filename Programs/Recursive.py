global i
i=0
def power(m,n):
     if i==n:
          return 1
     else:
          i+=1
          m=m+power(m,n)

     return m;


m=int(input("enter the value of m"))
n=int(input("enter the value of n"))
print("product=")
print(power(m,n))




          
