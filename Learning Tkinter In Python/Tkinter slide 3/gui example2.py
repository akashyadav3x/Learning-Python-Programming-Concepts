from tkinter import *
from tkinter.font import Font

root = Tk()
#root.geometry('600x400')
mf = Font(size=18)
l1 = Label(text='python is very usefull', bg='yellow', font=mf)
l2 = Label(text='java is one of the best languadge in software industry', bg='red', font=mf)
l1.pack(fill=X, padx=(0,40))
l2.pack(fill=X, padx=(40,0))

l3 = Label(text='python is very usefull', bg='yellow', font=mf)
l4 = Label(text='java is one of the best languadge in software industry', bg='red', font=mf)
l3.pack(fill=X, pady=(0,40))
l4.pack(fill=X, pady=(40,0))

root.mainloop()