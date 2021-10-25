from tkinter import *
root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = screen_width//2
height = screen_height//2
x_c = screen_width//4
y_c = screen_height//4
img = PhotoImage(file='D:/images/takeout.png')
root.config(bg='black')
root.iconphoto(root, img)
root.geometry(f"{width}x{height}+{x_c}+{y_c}")
root.resizable(False, False)
msg = "Exploring Tkinter"
root.title(msg)
lbl = Label(text='Python is most language')
lbl.pack()
root.mainloop()