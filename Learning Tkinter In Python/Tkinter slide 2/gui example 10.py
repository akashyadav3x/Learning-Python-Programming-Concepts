from tkinter import *

root = Tk()
#root.geometry('400x400')
x = StringVar()
lbl1 = Label(root, borderwidth=2, relief='solid', textvariable=x, font='Vardana 22 bold', height=6)
x.set("Python is a genral purpose programming languadge")
lbl1.config(bg='yellow')
lbl1.pack()
print(x.get())
root.mainloop()