from tkinter import *
from tkinter.font import Font

root = Tk()
#root.geometry('600x400')
mf = Font(size=18)
l1 = Label(text='hello akash you are learning python or not', bg='yellow', font=mf)
l2 = Label(text='Hello python', bg='red', font=mf, height=4)
l1.pack(fill=X, padx=20)
l2.pack(side=LEFT, pady=20)
#l2.pack(side=BOTTOM)

root.mainloop()