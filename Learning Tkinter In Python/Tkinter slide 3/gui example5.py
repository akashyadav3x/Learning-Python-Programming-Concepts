from tkinter import *
from tkinter.font import Font

root = Tk()
root.geometry('600x400')
l1 = Label(root, text="Label 1 : x=0, y=0", bg="red", fg="white")
l2 = Label(root, text="Label 2 : x=50, y=40", bg="blue", fg="white")
l3 = Label(root, text="Label 3 : x=75, y=80", bg="green", fg="white")
l4 = Label(root, text="Label 4 : x=25, y=100", bg="yellow", fg="white")
l1.place(x=0, y=0)
l2.place(x=50, y=50)
l3.place(x=100, y=100)
l4.place(x=150, y=150)
root.mainloop()
