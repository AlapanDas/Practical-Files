import csv
fw=open(r"C:\Users\clash\AppData\Local\Programs\Python\Python38\patient.csv",'r')
cs=csv.reader(fw)
next(cs)
for line in cs:
    if line[0][0]=='O' or line[0][-1]=='r' and int(line[1])>70:
        print(line[5])
fw.close()