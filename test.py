# for _ in range(int(input())):
#     l=['A','B','A']
#     n=len
#     for i in range(1,n+1):
#         print(*l[:n-i],*l[0],*l[n-i:-1])
for _ in range(int(input())):
    s=input()
    flag=0
    for i in range(0,len(s)):
        if s.count(s[:len(s)-i])==2:
            print(s[:len(s)-i])
            flag=1
            break
    if flag==0:
        print(-1)