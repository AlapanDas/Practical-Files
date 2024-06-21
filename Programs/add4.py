import pickle
r=[]
while True:
    S_Admno=int(input("Enter admission number"))
    S_Name=input("Enter name")
    Percentage=float(input("Enter percentage"))
    dta=[S_Admno,S_Name,Percentage]
    r.append(dta)
    ch=input("Enter MORE?")
    if ch=='n' or ch=='N':
        #csv is plain text file format used yo store tabular data on a spreadsheet or a data file
        break
f=open(r'C:\Users\clash\AppData\Local\Programs\Python\Python38\STUDENT_.dat',"wb+")
pickle.dump(r,f)
f.close()
