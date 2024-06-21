def atm(cash):#cash==10001
     print(cash)
     if cash>10000:
          print("above 10000")
          for i in range(3):
               print("good boy")
     else:
          print("below 10000")
     print("success")
     

n=int(input("enter withdrawn amount"))
atm(n)
