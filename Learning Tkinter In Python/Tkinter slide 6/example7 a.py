from tkinter import *
from tkinter import filedialog, messagebox


def showopen():
    # askopenfiles returns a string not ruple
    file_names = filedialog.askopenfiles(initialdir="d:/", title="Select your fav song",
                                         filetypes=[("mp3 files", "*.mp3")])
    str = ""
    if type(file_names) is tuple:
        for file in file_names:
            str += file + "\n"
            lbl.configure(text=str)
    else:
        messagebox.showinfo("Your selections", "You did not select any file")


root = Tk()
root.geometry("600x300")
btn = Button(root, text="Open Files", command=showopen)
lbl = Label(root, text="Your selected file names will appear here")
btn.pack()
lbl.pack()
root.mainloop()
