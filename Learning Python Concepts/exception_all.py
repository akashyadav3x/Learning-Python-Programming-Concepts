try:
    a=int(input("Enter a no "))
    b = int(input("Enter a no "))
    c=a/b
    print("Division is ",c)

except Exception:
    print("Somthing went rong:")
except BaseException:
    print("Baap of exceptions")