import csv
fw=open(r"C:\Users\clash\AppData\Local\Programs\Python\Python38\Programs\patient.csv",'r')
cs=csv.reader(fw)
next(cs)
for line in cs:
    if int(line[4])>250 and int(line[3])<125:
        print(line)
fw.close()
