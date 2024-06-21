def rotate1(mat):
    m=[]
    for i in range(3):
        fl=mat[i][-1]
        m.append(fl)
        m=m+mat[i][:-1]
    return m
def rotate2(mat):
    m=[]
    fl=mat[-1]
    m.append(fl)
    m=m+mat[:-1]
    return m
if __name__ == "__main__":
    C=int(input("Enter number of coloumns"))
    R=int(input("Enter number of rows"))
    matr = [[int(input()) for x in range (C)] for y in range(R)]
    print(matr)
    print(rotate1(matr))
    print(rotate2(matr))
    
