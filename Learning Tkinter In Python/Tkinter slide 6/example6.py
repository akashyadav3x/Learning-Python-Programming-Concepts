from tkinter import *
from tkinter import filedialog, messagebox


def showopen():
    filename = filedialog.askopenfiles(title='Select  song', initialdir='D:\\Audio Songs\\',
                           filetypes=[("mp3 songs","*.mp3"),("mp4 videos","*.mp4"),
                                      ("mkv videos",".mkv")])
    if filename != None:
        messagebox.showinfo("Your song", "You select a songs "+str(filename))
    else:
        messagebox.showinfo("message", "Your didnt select any songs")

root = Tk()
root.geometry("200x200")
btn = Button(root, text="Open File", command=showopen)
btn.pack()
root.mainloop()
