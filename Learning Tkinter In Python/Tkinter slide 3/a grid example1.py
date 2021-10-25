from tkinter import *

root = Tk()
l1 = Label(text='lable 1', bg='blue', fg='white')
l2 = Label(text='lable 2', bg='red', fg='white')
l3 = Label(text='lable 3', bg='black', fg='white')
l4 = Label(text='lable 4', bg='yellow', fg='white')
l1.grid(row=0, column=0)
l2.grid(row=0,column=1)
l3.grid(row=0, column=2)
l4.grid(row=1, column=1)
root.mainloop()