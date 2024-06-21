def size_letter():
    fw=open(r"C:\\Users\\clash\\AppData\\Local\\Programs\\Python\\Python38\\DATA.txt")
    for lines in fw:
        words=lines.split()
        for i in words:
            if len(i) < 4:
                print(i)
    fw.close()
size_letter()