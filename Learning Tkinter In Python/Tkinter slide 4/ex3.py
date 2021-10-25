from tkinter import *
count = 0
def counter():
    global count
    count = count + 1
    print(count, end=' ')
    lbl.config(text=str(count))


window = Tk()
window.geometry('200x200')
Button(window,text='click me', command=counter).pack()
lbl = Label(window, text=str(count))
lbl.pack()

window.mainloop()
print(count)