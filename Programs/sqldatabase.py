import mysql.connector as s
con=s.connect(host="root@localhost",user="clash",passwd=6969,database="alapan")
if con.is_connected():
    print("Successfully Connected")