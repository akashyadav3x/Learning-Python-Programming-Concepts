class Mymath:
    @staticmethod
    def add_nums(a,b):
        c=a+b
        return c
    @staticmethod
    def multi_numbs(a,b):
        c=a*b
        return c
    @staticmethod
    def divide_nums(a,b):
        c=a/b
        return c
add=Mymath.add_nums(45,67)
multiplay=Mymath.multi_numbs(7,98)
divid=Mymath.divide_nums(56,8)
print("Addition is : ",add)
print("Multiplay is : ",multiplay)
print("Division is : ",divid)