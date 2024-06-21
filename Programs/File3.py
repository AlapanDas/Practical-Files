fw=open(r"C:\\Users\\clash\\AppData\\Local\\Programs\\Python\\Python38\\Programs\\DIGIT.txt")
count=0
for lines in fw:
    words=lines.split()
    for i in words:
        for letters in i:
            if letters.isdigit():
                count+=1
print(count)   
fw.close()      