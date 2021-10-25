def show_msg():
    return "Welcome in python's world"

def show_in_lable():
    lbl = Label(root, text=show_msg()).pack()

from tkinter import *
root = Tk()
root.geometry('200x200')
b1 = Button(root, text='click me', command=show_in_lable).pack()
root.mainloop()
