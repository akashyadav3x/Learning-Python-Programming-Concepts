import tkinter
window = tkinter.Tk()
window.title('exirsize 1 from sca')
window.geometry('600x400')
lbl1 = tkinter.Label(window)
lbl1.pack()
msg = 'Welcome to python gui'
lbl1.config(text='Welcome to python', fg='blue', bg='red')
window.resizable(False, False)
window.configure(bg='yellow')
window.mainloop()