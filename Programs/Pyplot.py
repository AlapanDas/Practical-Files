fib=[0,1]
def fibonacci(n):
    if n<0:
        print("Invalid Input")
    elif n<=len(fib):
        return fibonacci(n-1)
    else:
          temp= fibonacci(n-1)  +    fibonacci(n-2)
          fib.append(temp)
          return temp

n=int(input("Enter the Number of term"))
print("The ",n,"th fibonacci term is",fibonacci(n))
