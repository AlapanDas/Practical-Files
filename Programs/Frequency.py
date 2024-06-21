def inpt():
    for i in range(5):
        m=int(input("Enter your marks"))
        l.append(m)
        if i ==4:
            for j in l:
                if j in done:
                    continue
                else:   
                    c=l.count(j)
                    done.append(j)
                    print("Frequency of ",j,"is ",c)

if __name__ == "__main__":
    l=[]
    done=[]
    inpt()
