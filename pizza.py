# cook your dish here
def solve(s,r,g):
    for j in s[2::2]:
        a=int(r)
        b=int(j)
        z=(a+b)%2
        r=str(z)
        g=g+r+r
    return g

def bintoDec(s,n):
    return(int(s[0:n],2))

t=int(input(""));
while(t>0):
    n=int(input(""));
    s=input("");
    r=s[0];
    g=r+r;
    g=solve(s,r,g)
    k=bintoDec(g,n)
    print(k%998244353)
    t=t-1