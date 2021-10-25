from tkinter import *

root = Tk()
#padding
lbl1 = Label(text='Python is Good', font=('times new roman', 18, 'bold'), bg='pink', height=2)
lbl1.pack(fill=X)
lbl2 = Label(text='Python is Good for c++', font=('times new roman', 18, 'bold'), bg='yellow', height=3)
lbl2.pack(fill=Y)
lbl3 = Label(text='java is Good', font=('times new roman', 18, 'bold'), bg='red', height=2)
lbl3.pack(padx=(20,0))
lbl4 = Label(text='J2EE is Good', font=('times new roman', 18, 'bold'), bg='blue', height=2)
lbl4.pack(fill=X,pady=(0,40))


root.mainloop()
