from tkinter import *

root = Tk()
root.title("Akash Yadav")
#root.geometry("600x600")
scree_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print(scree_width)
print(screen_height)

width = scree_width//2
height = screen_height//2
print("Half of the screen")
print(width)
print(height)

x_c = scree_width//4
y_c = screen_height//4
print("cordination of x and y")
print(x_c)
print(y_c)

root.geometry(f"{width}x{height}+{x_c}+{y_c}")
root.resizable(False, False)
img = PhotoImage(file="D:/images/success.png")
root.iconphoto(root, img)

root.mainloop()
