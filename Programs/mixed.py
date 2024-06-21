def transpose(matrix):
    tran=matrix
    m=len(matrix)
    n=len(matrix[0])
    for i in range(m):
        for j in range(n):
            tran[j][i]=matrix[i][j]
    return tran
def possible_date(count):
    l=[]
    for i in range(count):
        n=int(input("ENTER DATE(DAY NUMBER ONLY)")) 
        l.append(n)
    high=key=0
    for i in range(len(l)):
        if l.count(l[i])>high:
            high=l.count(l[i])
            key=l[i]
    print("THE POSSIBLE DATE WHICH IS OFFERED BY MOST IS ",key)
