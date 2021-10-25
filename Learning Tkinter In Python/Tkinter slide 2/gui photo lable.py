from tkinter import *
from tkinter.font import Font

root = Tk()
#root.geometry('400x400')
my_font = Font(size=18)
x = StringVar()

img = PhotoImage(file='D:/images/cash_on_del.png')
#print(img.__dict__)
lbl = Label(root,image=img, textvariable=x,text='Python is genral purpose language', compound=LEFT, font=my_font)
lbl.pack()
print(lbl.keys())
x.set("Python is fun")

root.mainloop()
