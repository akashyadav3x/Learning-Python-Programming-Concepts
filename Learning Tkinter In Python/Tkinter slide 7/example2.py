from tkinter import *

root = Tk()
def show():
	print(x.get())

x=StringVar()
cb=Checkbutton(root,text="Click Me", command=show, variable=x,onvalue="hi",offvalue="bye")
cb.deselect() # This is required to keep the Button deselected

root.mainloop()
