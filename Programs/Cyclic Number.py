def input(num):
     l=len(num)
     dgt=num.split()
     for i in range(l):
          n=dgt[i]*num
          if check(n,num)==1:
               flag=1
          else:
               flag=0
     if flag==1:
          print("cyclic number")
     else:
          print("not a cyclic Number")
#--------------------------------------------------------
def check(x,y):
     m=len(x)
     n=len(y)
     dgts=y.split()
     i=0
     if m==n:
          for i in range(m):
               d=num%10
               num=num/10
               if d in dgts:
                    flg=1
               else:
                    flg=0

     if flg==1:
          return 1
     else:
          return 0
     
n=int(input("Enter a number to check"))
input(n)
