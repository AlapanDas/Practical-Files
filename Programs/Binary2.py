def update_file(roll):
    import pickle
    f=open(r"C:\Users\clash\\AppData\Local\Programs\Python\Python38\Programs\\STOCK.DAT","rb+")
    flag=0
    s=pickle.load(f)
    for R in s:
        if R[0]==roll:
            s.remove(R)
            flag+=1
    if flag==0:
        print("Not found")
    f.seek(0)
    print("After Deleting")
    for k in s:
        print(k)
    f.close()
#-----------------------------------------------------
def showfile():
    import pickle
    f=open(r"C:\\Users\\clash\\AppData\\Local\\Programs\\Python\\Python38\\Student.dat","rb")
    rec=pickle.load(f)
    print(rec)
    f.close()     
#main:
roll=int(input("Enter the roll number"))
showfile()
update_file(roll)
