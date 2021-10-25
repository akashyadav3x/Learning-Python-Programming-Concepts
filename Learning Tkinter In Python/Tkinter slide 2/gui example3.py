from tkinter import *
import tkinter.font as tkFont

root = Tk()

myfont = tkFont.Font(weight='bold', size='22', family='times new roman', underline=1, overstrike=1)
lbl1 = Label(root, text='welcome to the world of python',fg='yellow', bg='black',font=myfont)
lbl1.pack()

root.geometry('600x400')
root.config(bg='yellow')
root.mainloop()