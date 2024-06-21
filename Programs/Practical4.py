def check(x):
        count=0
        for i in range(1,(x//2)+1):
            if x%i==0:
                count+=1
            if count==1:
                return False
            else:
                return True
def execute():
        n=int(input("Enter your Number"))
        a=b=0      
        for i in range(1,n+1):
            d=n%10
            if check(d)==True:
                a=a*10+d
            else:
                b=b*10+d
            n=n//10    
        print(a," ",b)
execute()