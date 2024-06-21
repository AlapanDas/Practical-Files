import csv
fw=open(r"C:\Users\clash\AppData\Local\Programs\Python\Python38\patient.csv",'r')
cs=csv.reader(fw)
next(cs)
L=[]
for line in cs:
    L.append(line[7])
print("Maximum Heart-Beat-",max(L),"Minimum Heart-Beat-",min(L))
fw.close()