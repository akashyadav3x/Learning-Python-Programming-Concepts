from tkinter import *

root = Tk()
root.geometry('200x200')

root.geometry('200x200')
root.bind("b",lambda e: root.config(bg='blue'))
root.bind("y",lambda e: root.config(bg='yellow'))
root.bind("r",lambda e: root.config(bg='red'))

root.mainloop()