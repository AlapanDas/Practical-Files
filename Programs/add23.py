import pickle
r=[]
while True:
    roll=int(input("Enter roll"))
    name=input("Enter name")
    cl=int(input("Enter class"))
    sec=input("Enter section")
    mb=int(input("Enter mbno"))
    mrk=int(input("Enter marks"))
    dta=[roll,name,cl,sec,mb,mrk]
    r.append(dta)
    ch=input("Enter MORE?")
    if ch=='n' or ch=='N':
        #csv is plain text file format used yo store tabular data on a spreadsheet or a data file
        break
f=open(r'C:\Users\clash\AppData\Local\Programs\Python\Python38\\Practical\\STUDENT.DAT',"wb")
pickle.dump(r,f)
f.close()
