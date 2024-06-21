import random

from numpy import bitwise_xor
S=0
count=0

T=int(input())

for i in range(T):    
    N=int(input())
    while(S<=(2**N)-1):
        x=random.randint(0,(2**N)-1)

        # now new score S= S|X
        S+=bitwise_xor(S,N) % (1000000007)
        count+=1
c= count % ((10**9) +7)
print(c)