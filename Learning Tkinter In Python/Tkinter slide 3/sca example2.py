import tkinter
root = tkinter.Tk()
root.geometry('200x200+100+200')
l1=tkinter.Label(root, text="Label 1 : x=0, y=0", bg="red", fg="white")
l2=tkinter.Label(root, text="Label 2 : x=50, y=40", bg="blue", fg="white")
l3=tkinter.Label(root, text="Label 3 : x=75, y=80", bg="green", fg="white")
l4=tkinter.Label(root, text="Label 4 : x=25, y=100", bg="yellow", fg="white")
l1.place(x=0, y=0)				#Output:
l2.place(x=50, y=40)
l3.place(x=75, y=80)
l4.place(x=25, y=100)
root.mainloop()
