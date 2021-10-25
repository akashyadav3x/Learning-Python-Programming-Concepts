from tkinter import *
from tkinter import font

root = Tk()
root.title("Login Window")
root.geometry('200x200+100+200')
my_font = font.Font(size=10, weight='bold')
# root.config(bg='black')
l1 = Label(root, text="Name:", font=my_font)
l2 = Label(root, text="Password:", font=my_font)
l3 = Button(root, text="Login", font=my_font)
l4 = Button(root, text="Quit", font=my_font)
e1 = Entry(root)
e2 = Entry(root)
c1 = Checkbutton(root, text="Keep me logged in", font=my_font)
l1.grid(row=0, column=0, sticky=E)
e1.grid(row=0, column=1, columnspan=2)
l2.grid(row=1, column=0, sticky=E)
e2.grid(row=1, column=1, columnspan=2)
c1.grid(pady=10, row=2, column=0, columnspan=2)
l3.grid(row=3, column=0, pady=10, padx=(20, 0))
l4.grid(row=3, column=1, pady=10)

root.mainloop()
