while True:
    try:
        a=int(input("Enter a no: "))
        b=int(input("Enter a no: "))
        c=a+b
        print("Sum is: ",a+b)
        c=a/b
        print("Division is: ",c)
        c=a*b
        print("Multiplication is ",a*b)
        c=a-b
        print("Substraction is ",c)
        c=a%b
        print("Mod is: ",c)
        break
    except ValueError:
        print("Enter a int only")
    except ZeroDivisionError:
        print("Inter a non zero values")
    except OverflowError:
        print("Enter a shoet values i for calculations")
    except Exception:
        print("Somthing went rong....Try agin!")


print("No exception is occered in this code....")