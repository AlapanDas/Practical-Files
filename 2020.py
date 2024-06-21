# from math import log
# for i in range(int(input())):
#     n=int(input())
#     x=input()
#     l=set([])
#     for j in x:
#          j=int(j)
#          if(j==0):
#               continue
#          temp=log(j)//log(2)
#          l.add(temp)
#     print(len(l))
     # Creating a Tuple
# with the use of loop
Tuple1 = ('A')
n = 5
print("\nTuple with a loop")
for i in range(int(n)):
     Tuple1=Tuple1.join((Tuple1,))
     print(Tuple1)