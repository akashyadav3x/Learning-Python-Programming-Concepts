def show_date_time():
    from datetime import datetime
    today = datetime.now()
    print(today)
    date = today.strftime('%M akash Yadav %Y')
    print(date)
    day = today.strftime('%d')
    mon = today.strftime('%b')
    year = today.strftime('%Y')
    print(day)
    print(mon)
    print(year)

def show_date_time1():
    from datetime import datetime
    today = datetime.now()
    date = today.strftime('%d-%b-%Y')
    time = today.strftime('%I:%S:%p')
    lbl = Label(root, text=date).pack()
    lbl2 = Label(root, text=time).pack()

from tkinter import *
root = Tk()
root.geometry('200x200')
Button(root, text='click me', command=show_date_time1).pack()
root.mainloop()
