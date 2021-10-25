from tkinter import messagebox
from tkinter import *

root = Tk()

messagebox.showinfo("Message Boxes", "You are learning tkinter in python")
messagebox.showerror("Error", "You are very bed at programming")
messagebox.showwarning("Warning!", "Are you sure about this")
root.destroy()
root.mainloop()