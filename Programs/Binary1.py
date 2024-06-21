def add_details():
    import pickle
    f=open(r"C:\\Users\\clash\AppData\\Local\\Programs\\Python\\Python38\bin1.bin","ab")
    while True:
        empno=int(input("Enter Employee Number"))
        name=input("Enter Employee Name ")
        add=input("Enter Address ")
        sal=int(input("Enter Salary "))
        string=str(empno)+name+add+str(sal)
        pickle.dump(string,f)
        ch=input("Enter MORE? ")
        if ch=='n'or ch=='N':
            break
    print("DONE!")
    f.close()
add_details()
