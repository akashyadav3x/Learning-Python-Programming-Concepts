while True:
    try:
        a=int(input("Enter a no: "))
        b=int(input("Enter a no: "))
        c=a/b
        print("Division is: ",c)
        break

    except (ValueError,ZeroDivisionError):
        print("Either you enter a 0 or you enter a non int value....try again!")