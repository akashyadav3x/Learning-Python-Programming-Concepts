from tkinter import *
import tkinter.font as tkFont

root = Tk()
root.geometry('600x400')

myfont = tkFont.Font(size=18)

lbl1 = Label(root, text='solid', font=myfont, borderwidth=3, relief='solid', width=23)
lbl2 = Label(root, text='flat', font=myfont, borderwidth=3, relief='flat', width=23)
lbl3 = Label(root, text='raised', font=myfont, borderwidth=3, relief='raised', width=23)
lbl4 = Label(root, text='sunken', font=myfont, borderwidth=3, relief='sunken', width=23)
lbl5 = Label(root, text='groove', font=myfont, borderwidth=3, relief='groove', width=23)
lbl5 = Label(root, text="ridge", font=myfont, borderwidth=3, relief="ridge", width=23)

lbl1.pack()
lbl2.pack()
lbl3.pack()
lbl4.pack()
lbl5.pack()

root.mainloop()
