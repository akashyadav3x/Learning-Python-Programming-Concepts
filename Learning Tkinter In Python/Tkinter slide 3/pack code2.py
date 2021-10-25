from tkinter import *
root = Tk()
lbl = Label(root, text='Python is robust', bg='yellow', height=3)
lbl.pack(ipadx=50)
lbl1 = Label(root, text='Python is robust', bg='yellow', height=3)
lbl1.pack(pady=10, ipady=50)
root.config(bg='black')
root.mainloop()