import mysql.connector
Con=mysql.connector.connect(host="127.0.0.1",user="clash",passwd="6969")
cur=Con.cursor()
com="CREATE TABLE  IF NOT EXISTS EMPLOYEE(EMPID VARCHAR(3),ENAME VARCHAR(10),SALARY INT(6),CITY VARCHAR(10),DEPT VARCHAR(15));"
cur.execute(com)
Con.commit()
stri=[["E01","ROHAN",55000,"DELHI","ACCOUNTANT"],["E05","DEPANJAN",60000,"KOLKATA","ACCOUNTANT"],["E03","RAVI",45000,"MUMBAI","CLERK"],["E06","KARAN",30000,"KOLKATA","CLERK"],["E04","AKASH",70000,"DELHI","MANAGER"]]
for i in range(5):
    com="insert into employee values('{}','{}',{},'{}','{}')".format(*stri[i])
    cur.execute(com)
    Con.commit()
cur.execute("SELECT * FROM EMPLOYEE WHERE CITY='{}'".format('KOLKATA'))
res=cur.fetchall()
print("EMPID","ENAME","SALARY","CITY","DEPT")
print(res[0][0],res[0][1],res[0][2],res[0][3],res[0][4])
print(res[1][0],res[1][1],res[1][2],res[1][3],res[1][4])
