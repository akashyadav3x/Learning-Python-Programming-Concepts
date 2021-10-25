from tkinter import *
from tkinter.font import Font

root = Tk()
root.geometry('400x400')
myFont = Font(size=18, family='times new roman')
l1 = Label(text='lable 1', bg='blue', fg='white', font=myFont)
l2 = Label(text='lable 2', bg='red', fg='white', font=myFont)
l3 = Label(text='lable 3', bg='black', fg='white', font=myFont)
l4 = Label(text='lable 4', bg='yellow', fg='white', font=myFont)
l1.grid(row=0, column=0)
l2.grid(row=1,column=1)
l3.grid(row=2, column=2)
l4.grid(row=3, column=3)
root.mainloop()