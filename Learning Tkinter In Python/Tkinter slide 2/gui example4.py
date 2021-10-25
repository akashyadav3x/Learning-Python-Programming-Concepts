from tkinter import *
import tkinter.font as tkFont

root = Tk()

root.geometry('600x400')
myfont = tkFont.Font(size=14, family='times new roman')
lbl1 = Label(root, text='Python is really very easy for beginners', width=36, font=myfont,bg='pink',fg='blue')
root.config(bg='black')
lbl1.pack()

root,mainloop()