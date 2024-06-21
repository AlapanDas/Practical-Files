import csv
fw=open(r"C:\Users\clash\AppData\Local\Programs\Python\Python38\patient.csv",'r')
cs=csv.reader(fw)
next(cs)
List =list(cs)
List=List[::-1]
for line in List:
    print(line)
fw.close()