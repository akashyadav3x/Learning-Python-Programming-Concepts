from tkinter import *
root = Tk()
lbl = Label(root, text='Python is robust', bg='yellow', height=3)
lbl.pack(fill=X, padx=20)
lbl1 = Label(root, text='Python is robust', bg='yellow', height=3)
lbl1.pack(fill=X, pady=20)
root.config(bg='black')
root.mainloop()