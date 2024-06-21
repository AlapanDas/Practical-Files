l=[]
n=int(input("Enter the number of participants"))
if n>3 and n<11:
    key=input("Enter the Answer Key in String").upper()
    for i in range(n):
        st=str(input("Enter the answers in string"))
        l.append(st.upper())
    score=0
    marks=[]
    print(n)
    for i in range(n):
        print("Participant ",l[i])
        for j in range(5):
            if l[i][j]==key[j]:
                score+=1
            marks.append([score,i])
    print("key",key)
    marks.sort(reverse=True)
    print("Maximum Score-  Participant",marks[0][1])
else:
    print("Wrong Input")