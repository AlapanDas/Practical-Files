fw=open(r"C:\\Users\\clash\\AppData\\Local\\Programs\\Python\\Python38\\source.txt",'r')
fw2=open(r"C:\\Users\\clash\\AppData\\Local\\Programs\\Python\\Python38\\target.txt",'w')
f=fw.readlines()
for i in f:
    if i[0].islower():
        continue
    else:
        fw2.write(i)
fw.close()
fw2.close()
