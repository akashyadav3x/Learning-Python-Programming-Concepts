# Bind method
from tkinter import *

root = Tk()
root.geometry('200x200')


def even(e):
    root.config(bg='black')


def even1(e):
    root.config(bg='white')

def even2(e):
    root.config(bg='yellow')

btn = Button(root, text='click me')
btn.pack()
btn.bind('<Button>', even)
btn.bind('<Button-3>', even1)
root.bind("<Escape>", even2)

root.mainloop()
