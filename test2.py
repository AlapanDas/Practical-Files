for i in range(int(input())):
    a,b=map(int,input().split())
    alapan_one=a//2
    alapan_two=b//2
    if a%2==1 and b%2==1:
        print("-1")
    else:
        if a%2==0 and b%2==0:
            print("a"*alapan_one+"b"*b+"a"*alapan_one)
            print("b"*alapan_two+"a"*a+"b"*alapan_two)
        else:
            if a%2==1:
                print(alapan_two*"b"+"a"*a+alapan_two*"b")
                print((alapan_two//2)*"b"+"a"*alapan_one+"b"*alapan_two+"a"*alapan_one+(alapan_two//2)*"b")
            else:
                print(alapan_one*"a"+"b"*b+alapan_one*"a")
                print(alapan_two*"b"+"a"*alapan_one+"b"+"a"*alapan_one+alapan_two*"b")