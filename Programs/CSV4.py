import csv
fw=open(r"C:\Users\clash\AppData\Local\Programs\Python\Python38\patient.csv",'r')
cs=csv.reader(fw)
next(cs)
L=[]
for line in cs:
    L.append([line[4],line[0]])
L=sorted(L)
L=L[::-1]
for i in L:
    print(i[1])
fw.close()
