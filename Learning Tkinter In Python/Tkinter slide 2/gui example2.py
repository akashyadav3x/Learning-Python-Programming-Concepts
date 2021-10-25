from tkinter import *
window = Tk()
lbl1 = Label(window,text='python is my fav language', font='Arial 22 bold', fg='red', bg='yellow')
lbl1.pack()
window.geometry('600x400')

lbl2 = Label(window, text='java is an importent languadge', font='vardana 19 italic')
lbl2.pack()

lbl3 = Label(window, text='c++ is my second prefirred languadge', fg='pink', bg='black', font=('Times new roman', 18 , 'bold')).pack()
window.mainloop()