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
    global my_data
    my_data = data3
    l3.config(text=data3, font="Arial 18 bold")

my_data = ""


def Quit(e):
    root.destroy()

    def new_add(e):
        new_l3 = Label(new_root)
        new_l3.pack()
        new_l3.config(text="Thank You"+'\n'+"Mr."+my_data, font="Arial 18 bold")

    new_root = Tk()
    new_root.geometry('400x400')
    new_root.config(bg='yellow')

    nb1 = Button(new_root, text="Press Me")
    nb1.pack()
    nb1.bind('<Button>', new_add)


l3 = Label()
l3.grid(row=2, column=0, columnspan=2, sticky=W)

e1.insert(0, "Akash")
e2.insert(0, "Yadav")

b1 = Button(root, text='show')
b1.bind("<Button>", add)

b1.grid(row=4, column=0)
b2 = Button(root, text='Quit')
b2.grid(row=4, column=1)

b2.bind("<Button>", Quit)



root.mainloop()