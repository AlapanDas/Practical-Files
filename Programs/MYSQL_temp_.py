import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password="6969",database="alapan")
cur=con.cursor()
cur.execute("create table if not exists Employee(EMPID varchar(10),ENAME varchar(20),SALARY int,CITY varchar(20),DEPT varchar(15))")
con.commit()
choice=row=None
while choice!=0:
    print("1.ADD RECORD")
    print("2.DISPLAY RECORD")
    print("3.SEARCH")
    print("4.UPDATE")
    print("5.DELETE")
    print("0.EXIT")
    choice=int(input("Enter choice : "))
    if choice==1:
        e=input("Enter Employee ID:")
        n=input("Enter name:")
        s=int(input("Enter Salary:"))
        c=input("Enter city :")
        d=input("Enter department:")
        query="insert into Employee values ('{}','{}',{},'{}','{}')".format(e,n,s,c,d)
        cur.execute(query)
        con.commit()
        print("##Data Saved##")
    elif choice==2:
        query="select * from Employee"
        cur.execute(query)
        result=cur.fetchall()
        print("%10s"%"EMPID","%20s"%"ENAME","%10s"%"SALARY","%15s"%"CITY","%15s"%"DEPT")
        for row in result:
            print("%10s"%row[0],"%20s"%row[1],"%10s"%row[2],"%15s"%row[3],"%15s"%row[4])
    elif choice == 3 :
        city = input("ENTER CITY TO SEARCH : ")
        query="select * from Employee where CITY='{}'".format(city)
        cur.execute(query)
        result = cur.fetchall()
        if cur.rowcount == 0 :
            print("Sorry!CITY not found")
        else:
            print("%10s"%"EMPID","%20s"%"ENAME","%10s"%"SALARY","%15s"%"CITY","%15s"%"DEPT")
        for row in result:
            print("%10s"%row[0],"%20s"%row[1],"%10s"%row[2],"%15s"%row[3],"%15s"%row[4])
    elif choice == 4:
            e1 = input("ENTER EMPID TO UPDATE :")
            query="select * from Employee where empid='{}'".format(e1)
            cur.execute(query)
            result = cur.fetchall()
            if cur.rowcount==0:
                print("Sorry! EMPID not found ")
            else:
                print("%10s"%"EMPID","%20s"%"ENAME","%10s"%"SALARY","%15s"%"CITY","%15s"%"DEPT")
            for row in result:
                    print("%10s"%row[0],"%20s"%row[1],"%10s"%row[2],"%15s"%row[3],"%15s"%row[4])
            choice=input("\n## ARE YOUR SURE TO UPDATE ? (Y) :")
            if choice.lower()=='y':
                   print("== YOU CAN UPDATE ONLY DEPT,SALARY AND CITY ==")                   
                   d = input("ENTER NEW DEPARTMENT,(LEAVE BLANK IF NOT WANT TO CHANGE ) : ")
                   if d=="":
                      d=row[4]
                   s = int(input("ENTER NEW SALARY,(LEAVE BLANK IF NOT WANT TO CHANGE ) : "))
                   if s == 0:
                      s=row[2]
                   c = input("ENTER NEW CITY,(LEAVE BLANK IF NOT WANT TO CHANGE ) : ")
                   if c == "":
                      c=row[3]
                   query="update Employee set dept='{}',salary={},city='{}' where empid='{}'".format(d,s,c,e1)
                   cur.execute(query)
                   con.commit()
                   print("## RECORD UPDATED ## ")
    elif choice == 5:
            e2 = input("ENTER EMPID TO DELETE :")
            query="select * from Employee where empid='{}'".format(e2)
            cur.execute(query)
            result = cur.fetchall()
            if cur.rowcount==0:
                print("Sorry! EMPID not found ")
            else:
                print("%10s"%"EMPID","%20s"%"ENAME","%10s"%"SALARY","%15s"%"CITY","%15s"%"DEPT")
            for row in result:
                    print("%10s"%row[0],"%20s"%row[1],"%10s"%row[2],"%15s"%row[3],"%15s"%row[4])
            choice=input("\n## ARE YOUR SURE TO DELETE ? (Y) :")
            if choice.lower()=='y':
                   query="delete from employee where empid='{}'".format(e2)
                   cur.execute(query)
                   con.commit()
                   print("## RECORD DELETED SUCCESSFULLY !!! ## ")
    elif choice==0:
        con.close()
        print("##EXIT##")
    else:
        print("##INVALID CHOICE##")