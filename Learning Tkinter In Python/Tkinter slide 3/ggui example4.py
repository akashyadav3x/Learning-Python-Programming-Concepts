from tkinter import *
from tkinter.font import Font

root = Tk()
#root.geometry('600x400')
l1 = Label(text='python is easy', bg='yellow', font='Arial 18 bold')
l2 = Label(text='java is fun', bg='red', font='vardana 19 bold')
l1.pack(ipadx=50)
l2.pack(ipadx=10)

root.mainloop()