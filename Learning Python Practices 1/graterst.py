a, b, c = input("Enter 3 int: ").split()
a=int(a)
b=int(b)
c=int(c)

if a>b:
    if a>c:
        print("{0} is greatest".format(a))
    else:
        print("{0} is grater".format(c))
else:
    if b>c:
        print("{0} is grater".format(b))
    else:
        print("{0} is grater".format(c))
