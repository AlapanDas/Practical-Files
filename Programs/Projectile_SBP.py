import math
print("This program is to calculate the various measurement of projectile motion")
print("Press  'OK' to start ")
if(input()=='OK'):
        print("Enter initial speed")
        u=int(input())
        print("Enter Angle of Projection")
        th=int(input())
        print("Press 1 for calculating Height")
        print("Press 2 for calculating Horizontal Range")
        print("Press 3 for calculating trime of Flight")
        if(int(input("Enter choice"))==1):
            H=(u**2*(math.sin(th)))/20
            print(H)
        elif(int(input("Enter Choice"))==2):
            R=(u**2*(matn.sin(2*th)))/10
            print(R)
        else:
            T=(2*u*(math.sin(th)))/10
            print(T)
else :
    print("Thank you for visiting our Program")
    
