while(True):

    try:
        a=int(input("Enter a no: "))
        b=int(input("Enter a no: "))
        c=a/b
        print("Division is: ",c)
        break

    except ValueError:
        print("Enter a Integers only")
    except ZeroDivisionError:
        print("Enter a non Zero value for calculation")

print("Everything is fine")