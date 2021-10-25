from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

def divide(e):
    try:
        e3.delete(0, END)
        a = int(e1.get())
        b = int(e2.get())
        c = a / b
        e3.insert(0, c)
    except ZeroDivisionError:
        messagebox.showerror("Zero devision error", "Denominitor should not 0")
    except ValueError:
        messagebox.showinfo('Value Error', 'Value should be int only')

def exit(e):
    ans = messagebox.askokcancel("Question", "Are you sure you want to cancle")
    if ans is not False:

        name = simpledialog.askstring(title='Age', prompt='Waht is you name?', initialvalue='User Ji')
        messagebox.showinfo("BYY", "Have a good day "+name)
        root.destroy()
        '''
    ans = messagebox.askquestion("Question", "What is your age?")
    if type(ans) is int:
        messagebox.showinfo("Message", "thank you ")
        '''


root = Tk()

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)

cal = Button(root, text='Divide')
cal.bind("<Button>", divide)

quit = Button(root, text='Quit')
quit.bind("<Button>", exit)
e1.pack()
e2.pack()
e3.pack()
cal.pack()
quit.pack()

root.mainloop()
