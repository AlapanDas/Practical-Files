def project():
    import mysql.connector as mycon
    from tkinter import Tk,Button,Label
    import png
    import pyqrcode
    from PIL import Image,ImageTk
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    con=mycon.connect(host="localhost",user="root",passwd="6969",database="alapan",auth_plugin='mysql_native_password')
    cur=con.cursor(buffered=True)
    #MAIN PART
    while(True):
        print("""Which movie do u want to watch \n 1. Dil Bechara \n 2. 3 Idiots \n 3. Dhammal \n 4. Harry Potter \n 5. Endgame \nPlease enter your choice!""")
        ch=(input("->"))
        mov={'1':"Dil Bechara",'2':"3 Idiots",'3':"Dhammal",'4':"Harry Potter",'5':"Endgame"}
        movie=mov[ch]
        cost=250
        print("""Select City \n A.Kolkata \n B.Delhi \n C.Mumbai \n D.Bangalore \n E.Hyderabad""")
        ch1=input("->")
        di={'A':"KOLKATA",'B':"DELHI",'C':"MUMBAI",'D':"BANGALORE",'E':"HYDERABAD"}
        city=str(di[ch1])+str(ch)
        st="SELECT HALLS FROM "+str(city)+";"
        cur.execute(st)
        con.commit()
        res=cur.fetchall()
        k=1
        print('%10s'%"Seats",'%20s'%"Halls")
        for row in res:
            print('%10s'%k,'%20s'%row)
            k+=1
        print("ENTER YOUR CHOICE")
        ch2=int((input("->")))
        hall=str(res[ch2-1][0])
        st2="select * from "+str(city)+" where halls='{}';".format(hall)
        cur.execute(st2)
        con.commit()
        res2=cur.fetchall()
        print('%10s'%res2[0][0],'%10s'%res2[0][1])
        print("Please select the number of seats from the avaliable seats given above")
        ch3=int(input("->"))
        st3="SELECT SEATS FROM "+str(city)+" WHERE HALLS='{}';".format(city,hall)
        cur.execute(st3)
        con.commit()
        print("SELECT TIME \nP.MORNING \nQ.AFTERNOON \nR.NIGHT")
        ch4=input("Enter your choice->")
        di2={'P':"MORNING",'Q':"AFTERNOON",'R':"NIGHT"}
        tme=di2[ch4]
        print("SELECT TIER \n I.BRONZE \n II.SILVER \n III.GOLD ")
        ch5=input("->")
        if ch5=='II':
            cost+=100
        elif ch5=="III":
            cost+=200
        print("Do u want to confirm ? Y/N")
        print("Movie-",movie,"\nCity-",city,"\nHall-",str(res[ch2-1][0]),"\nNo.of Seats",ch3,"\nShow-",tme,"\nCategory-",cost)#MOVIE,CITY,HALL,SEATS,TIME,TIER 
        ch6=input("->")
        if ch6[0].upper()=='Y':
            #here we have to change the seat number
            st3="UPDATE "+city+" SET SEATS=SEATS-{} WHERE HALLS='{}' ;".format(ch3,res[ch2-1][0])            
            cur.execute(st3)
            con.commit()
            if ch==1:
                url="https://in.bookmyshow.com//movies/dil-bechara/ET00098454"
            elif ch==2:
                url="https://in.bookmyshow.com/movies/3-idiots/ET00001611"
            elif ch==3:
                url="https://in.bookmyshow.com/movies/dhamaal/ET00000016"
            elif ch==4:
                url="https://in.bookmyshow.com/movies/harry-potter-and-the-deathly-hallows-part-2/ET00007363"
            else:
                url="https://in.bookmyshow.com/movies/avengers-endgame/ET00090482"
            qrc=pyqrcode.create(url)
            print("Scan the qrcode saved un your python directory and scan to complete payment")
            qrc.png('myqr.png', scale = 8)
            root=Tk()
            root.title("Movie Ticket Booking System")
            img=ImageTk.PhotoImage(Image.open('myqr.png'))
            my_label=Label(image=img)
            my_label.pack()
            button=Button(root,text="Cost=%s Payment Done"%(cost),command=root.quit)
            button.pack()
            root.mainloop() 
            break
        else:
            print(" THANK YOU,PLEASE VISIT AGAIN")
            break
    con.close()
if __name__=='__main__':
    print("WELCOME TO MOVIE TICKET BOOKING SYSTEM")
    project()