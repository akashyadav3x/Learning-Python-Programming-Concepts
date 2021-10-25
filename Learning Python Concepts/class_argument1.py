class Emp:
    def __init__(self,age,name,salary):
        self.age=age
        self.name=name
        self.salary=salary

    def __init__(self,age,name,salary):
        self.age = age
        self.name = name
        self.salary = salary

    def __init__(self, age, name):
        self.age = age
        self.name = name

emp1 = Emp(23,'Akash')
print(emp1.age,emp1.name)
emp2=Emp(45,"yadav",6000)
print(emp2.age,emp2.name,emp2.salary)