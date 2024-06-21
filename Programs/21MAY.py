def rshift():
     arr=[1,2,3,4]
     n=int(input("Enter n"))
     l=[]
     l=l.extend(arr[n:])
     l=l.extend(arr[:n])
     print(l)
rshift()
