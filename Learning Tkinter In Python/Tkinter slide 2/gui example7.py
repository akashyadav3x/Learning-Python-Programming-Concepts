from tkinter import *
from tkinter.font import Font

print(TkVersion)
root = Tk()

root.geometry('600x600')

img = PhotoImage(file='D:/images/success.png')

myfont = Font(size=18, weight='bold')
lbl1 = Label(text='Python is my love',borderwidth=8,relief='raised', height=4,
             width=23, font=myfont, bg='yellow', anchor='nw')


lbl2 = Label(text='my image', font=myfont, image=img,relief='raised', height=6, width=23)
lbl2.pack()


lbl1.pack()

root.mainloop()