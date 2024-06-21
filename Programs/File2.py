#write a program to count all lines in ABC.txt having 'a' as last character.
fw=open("C:\\Users\\clash\\AppData\\Local\\Programs\\Python\\Python38\\ABC.txt")
count=0
f=fw.readlines()
for line in f:
    line=line.rstrip('\n')
    if line[-1]=='a':
        count+=1
print(count)
fw.close()