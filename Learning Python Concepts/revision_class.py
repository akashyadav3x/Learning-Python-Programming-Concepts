class Emp:
    def __init__(self,age,name,sal):
        self.__age=age
        self.__name=name
        self.__sal=sal

    def __show(self):
        print(self.__age,self.__name,self.__sal)

    def output(self):
        self.__show()

    def __str__(self):
        return f"Age is:{self.__age},Name is:{self.__name},Salary is:{self.__sal}"

    def  __del__(self):
        print("Destrattor is called in your class")

e=Emp(25,'Akash Yadav',50000)
print(e)
t=e
del e
print(t)
print("Hello")
del t
#t.output()
print("Hiii")