from tkinter import *
from tkinter.font import Font

root = Tk()
root.geometry('600x400')
myFont = Font(size=14, family='Times new roman', weight='bold')
root.config(bg='pink')
#print(myFont.__init__)
l1 = Label(root, text='Number Addition Program    ',font='Vardana 19 bold')
l1.grid(row=0, column=0, columnspan=3)
print(l1.keys())

l2 = Label(root, text='First Number :', font=myFont)
l2.grid(row=1, column=0)
e1 = Entry(root,insertwidth=10)
print(e1.keys())
e1.grid(row=1, column=1, sticky=E+W)


l3 = Label(root, text='Second Number :', font=myFont)
l3.grid(row=2, column=0)
e2 = Entry(root)
e2.grid(row=2, column=1, sticky=E+W)

b1 = Button(text='Add')
b1.grid(row=3, column=0, sticky=E+W, padx=10)

b2 = Button(text='clear')
b2.grid(row=3, column=1, sticky=E+W, padx=10)

b3 = Button(text='Quit')
b3.grid(row=3, column=2, sticky=E+W)

root.mainloop()