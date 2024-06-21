import pickle        
def COSTLY():
    f=open(r"C:\Users\clash\AppData\Local\Programs\Python\Python38\Programs\STOCK.DAT","rb")
    fw=pickle.load(f)
    for rec in fw:
        if int(rec[1])>1000:
            print("Name-",rec[0]," Price-",rec[1])
    f.close()
def showfile():
    import pickle
    f=open(r"C:\Users\clash\AppData\Local\Programs\Python\Python38\Programs\STOCK.DAT","rb")
    rec=pickle.load(f)
    print(rec)
    f.close()
 #calling function:
showfile()
COSTLY()