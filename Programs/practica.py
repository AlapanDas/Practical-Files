import csv
def answer_key():  
    key=['D','C','C','A','B']   
    f=open(r'C:\Users\clash\AppData\Local\Programs\Python\Python38\Programs\details.csv','r')
    fw=csv.reader(f)
    for line in fw:
        if line[1]==key[0] and line[2]==key[1] and line[3]==key[2]and line[4]==key[3] and line[5]==key[4]:
            print(*line)
            x=line
        else:
            print(*line)
    print("correct =",*x)
answer_key()
