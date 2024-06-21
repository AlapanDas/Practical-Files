global i

def fibo(n):
     i=2
     i+=1
     if i==n:
          return 1
     else:
          term= fibo(i-1)+fibo(i-2)
     print(term)

     
