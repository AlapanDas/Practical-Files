import pickle
f=open(r"C:\Users\clash\AppData\Local\Programs\Python\Python38\Programs\STOCK.DAT","wb")
L=[['Apple',1280],['Motorola',1500],['Blackberry',999]]
pickle.dump(L,f)
f.close()