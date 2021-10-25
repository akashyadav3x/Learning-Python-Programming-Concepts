import tkinter

root = tkinter.Tk()
l1 = tkinter.Label(root, text="Red Sun", bg="red", fg="white")
l2 = tkinter.Label(root, text="Green Grass", bg="green", fg="white")
l3 = tkinter.Label(root, text="Blue Sky", bg="blue", fg="white")
l1.pack(padx=5, pady=5, side=tkinter.LEFT)
l2.pack(padx=5, pady=5, side=tkinter.LEFT)
l3.pack(padx=5, pady=5, side=tkinter.LEFT)
root.mainloop()
#Output:
