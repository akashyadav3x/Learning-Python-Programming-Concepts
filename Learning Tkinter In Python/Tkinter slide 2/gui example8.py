from tkinter import *
from tkinter.font import Font

print(TkVersion)
root = Tk()

root.geometry('600x600')

str_obj = StringVar()

lbl1 = Label(root, relief='solid', borderwidth=3, textvariable=str_obj)
lbl1.pack()
str_obj.set('Python is the way of changing the programmers industry')
n = str_obj.get()
str_obj.set("Teri jay ho")
m = str_obj.get()
print(n)
print(m)


root.mainloop()