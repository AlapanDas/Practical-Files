def admission():
    import pickle
    f=open(r"C:\Users\clash\AppData\Local\Programs\Python\Python38\Programs\STUDENT_.DAT","rb")
    s=pickle.load(f)
    for r in s:
        var=r[2]
        if var > 75:
            print(*r)
    f.close()
def showfile():
    import pickle
    f=open(r"C:\Users\clash\AppData\Local\Programs\Python\Python38\Programs\STUDENT_.DAT","rb")
    rec=pickle.load(f)
    for i in rec:print(*i)
    f.close()
#main:
showfile()
admission()

