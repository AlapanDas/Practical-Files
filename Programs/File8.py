count=0
fw=open(r"C:\\Users\\clash\\AppData\\Local\\Programs\\Python\\Python38\\SPE.txt")
f=fw.readline()
for i in range(len(f)):
    if f[i].isalnum():
        continue
    else:
        count+=1
print(count)