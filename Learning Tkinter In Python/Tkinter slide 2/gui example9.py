from tkinter import *

root = Tk()
root.geometry('600x400')
lbl = Label(text='hello', fg='yellow', bg='black', width=23,
            font=('times new roman', 18, 'bold'), anchor='nw', height=4)
lbl.pack()
root.config(bg='pink')
print(lbl.keys())
print(lbl['bg'])

if lbl['bg']=='black':
    lbl['bg']='red'

root.mainloop()