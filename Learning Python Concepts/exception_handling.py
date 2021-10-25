#program for dividing by 0
a=int(input("Enter a int: "))
b=int(input("Enter a int: "))
try:
    c=a/b
    print("Their devision is: ",c)
    import math
    ans=math.exp(10000)
    print("Ans is: ",ans)
except ZeroDivisionError:
    print("Give a non zero value for calculation")
except ArithmeticError:
    print("give a short value for calculations")
else:
    print("Program has no exception")