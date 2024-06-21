#Write a function to open the text file ABC.txt and count the number of words starting from "the-"like they them
def count_the():
    fw=open(r"C:\\Users\\clash\AppData\\Local\\Programs\\Python\\Python38\\ABC.txt","r")
    count=0
    for line in fw:
        word=line.split()
        for i in word:
            if i[0:3]=='the':
                count+=1
    print(count)  
count_the()