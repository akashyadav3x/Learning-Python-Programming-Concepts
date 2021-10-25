from tkinter import *
'''
def red():
    lbl['bg']='red'
def green():
    lbl['bg']='green'
def yellow():
    lbl['bg'] = 'yellow'
'''
root = Tk()
root.geometry('200x200')
lbl = Label(root, height=6,width=20, bg='white')
lbl.grid(row=0, column=0, padx=20, columnspan=3)
b1 = Button(root, command=lambda : lbl.config(bg='red'), text='red').grid(row=1, column=0, padx=10)
b2 = Button(root, command=lambda : lbl.config(bg='green'), text='green').grid(row=1, column=1)
b3 = Button(root, command=lambda : lbl.config(bg='yellow'), text='yellow').grid(row=1, column=2)

root.mainloop()