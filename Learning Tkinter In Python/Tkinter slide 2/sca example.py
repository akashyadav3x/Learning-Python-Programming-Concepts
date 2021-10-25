import tkinter
import tkinter.font as tkFont

root = tkinter.Tk()
root.geometry("400x400")
myfont = tkFont.Font(size="22")
lbl1 = tkinter.Label(root, text="solid", font=myfont, borderwidth=2, relief="solid", width=20)
lbl2 = tkinter.Label(root, text="flat", font=myfont, borderwidth=2, relief="flat", width=20)
lbl3 = tkinter.Label(root, text="raised", font=myfont, borderwidth=2, relief="raised", width=20)
lbl4 = tkinter.Label(root, text="sunken", font=myfont, borderwidth=2, relief="sunken", width=20)
lbl5 = tkinter.Label(root, text="ridge", font=myfont, borderwidth=2, relief="ridge", width=20)
lbl6 = tkinter.Label(root, text="groove", font=myfont, borderwidth=2, relief="groove", width=20)
lbl1.pack()
lbl2.pack()
lbl3.pack()
lbl4.pack()
lbl5.pack()
lbl6.pack()
root.mainloop()
