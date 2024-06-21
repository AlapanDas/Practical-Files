def printtext():
    global e
    string = e.get()  
    print(string)

from tkinter import *
root = Tk()
root.title('Name')
lbl=Label(root,text="Which movie do u want to watch 1. Dil Bechara 2. 3 Idiots 3. Dhammal 4. Harry Potter 5. Endgame Please enter your choice!")
lbl.pack()
e = Entry(root)
e.pack()
b = Button(root,text='Proceed',command=printtext)
b.pack(side='bottom')
root.mainloop()