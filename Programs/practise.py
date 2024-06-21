f=open(r"C:\Users\clash\AppData\Local\Programs\Python\Python38\Practical\BINARY.csv",'r')
import csv
fw=csv.reader(f)
next(fw)
for i in fw:
    if i[0][0]=='a' and int(i[-1])>2021:
        print(i)
f.close()
