class Person:
    def __init__(self,age,name):
        self.__age=age
        self.__name=name
        print("Person constructor s called")
    def __str__(self):
        return  f"Age is:{self.__age},Name is:{self.__name}"

class Emp(Person):
    def __init__(self,age,name,id,sal):
        super().__init__(age,name)
        self.__id=id
        self.__sal=sal
        print("Emp constructor is called")
    def income(self):
        return self.__sal
    def __str__(self):
        var1=super().__str__()
        return f"{var1},Id is:{self.__id},salary is:{self.__sal}"

class Manager(Emp):
    def __init__(self,age,name,id,sal,bonus):
        super().__init__(age,name,id,sal)
        self.__bonus=bonus
        print("Manager constructor is called")
    def income(self):
        total=super().income() + self.__bonus
        return total
    def __str__(self):
        var2=super().__str__()
        return f"{var2},\nTotal salary is of the manager is:{self.income()}"

m = Manager(25,'Aman',101,8000,500)
print("==========================================================")
print(m)
print("===========================================================")
print("Manager ki salary is: ",Emp.income(m))
print("Manager ki income is: ",m.income())