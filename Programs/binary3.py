def showfile():
    import pickle
    f=open(r"C:\\Users\\clash\\AppData\\Local\\Programs\\Python\\Python38\\Student.dat","rb")
    rec=pickle.load(f)
    for r in rec:
        print(r)
    f.close()

def update_marks(roll):
    import pickle
    f=open(r"C:\\Users\\clash\\AppData\\Local\\Programs\\Python\\Python38\\Student.dat","rb+")
    s=pickle.load(f)
    for r in s:
        if int(r[0]) ==roll:
            r[5]=int(input("Enter the new marks"))
            
    f.seek(0)
    pickle.dump(s,f)
    print("marks updated")
    f.close()
#main:
roll=int(input("Enter roll"))
showfile()
update_marks(roll)
showfile()
