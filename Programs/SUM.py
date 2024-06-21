def main():
     num=int(input("enter the number"))
     if((num%10)**len(num))==sum(num):
          print("hello")
def sum():
     i,d=0,0
     sm=0
     for i in range(0,len(num)):
          d=num%10
          sm+=d
          num/=10
     return sm

