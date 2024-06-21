def vowelchk():
    fw=open(r"C:\\Users\\clash\\AppData\\Local\\Programs\\Python\\Python38\\ORIGIN.txt")
    fw2=open(r"C:\\Users\\clash\\AppData\\Local\\Programs\\Python\\Python38\\NEW.txt",'w')
    f=fw.readlines()
    for line in f:
        line=line.rstrip('\n')
        if line[0]in ['a','e','i','o','u','A','E','I','O','U']:
            fw2.write(line +'\n')
    fw.close()
    fw2.close()

vowelchk()




