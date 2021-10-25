from tkinter import *

root = Tk()
root.geometry('200x200')

l1 = Label(root, text="First Name:")
l2 = Label(root, text="Last Name:")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

e1 = Entry()
e2 = Entry()
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


def add(e):
    data1 = e1.get()
    data2 = e2.get()
    data3 = data1 + " " + data2
    l3.config(text=data3, font="Arial 18 bold")


l3 = Label()
l3.grid(row=2, column=0, columnspan=2, sticky=W)

e1.insert(0, "Akash")
e2.insert(0, "Yadav")

b1 = Button(root, text='show')
b1.bind("<Button>", add)

b1.grid(row=4, column=0)
b2 = Button(root, text='Quit')
b2.grid(row=4, column=1)

b2.bind("<Button>", lambda e: root.destroy())



root.mainloop()