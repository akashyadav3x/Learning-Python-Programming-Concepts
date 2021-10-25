from tkinter import *
root = Tk()

lbl1 = Label(root, text="Python is a genral purpose languadge", fg='blue', bg='yellow')
lbl1.pack()
lbl2 = Label(root, text="Java is an importent", fg='yellow', bg='black')
lbl2.pack()

lbl1.config(text='python is a good for development', fg='black', bg='pink')
lbl2.configure(text='java does very well on the secure web applications', fg='yellow', bg='red')

root.geometry('600x400')
root.mainloop()