from tkinter import *
from tkinter.font import Font

root = Tk()
root.geometry('400x400')
myFont = Font(size=12)

l1 = Label(text="Name:", font=('Times new roman', 18, 'bold'))
l2 = Label(text="password:", font=('Times new roman', 18, 'bold'))
e1 = Entry(root, font=myFont)
e2 = Entry(root, font=myFont)
b1 = Button(text='log in', font=myFont)
b2 = Button(text='Quit', font=myFont)
print(l1.keys()[0:10])
print(l1.keys()[10:20])
print(l1.keys()[20:30])

l1.grid(row=0, column=0, sticky=W)
e1.grid(row=0, column=1, columnspan=2)
l2.grid(row=1, column=0)
e2.grid(row=1, column=1, columnspan=2)
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)

root.mainloop()