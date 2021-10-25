class Emp:
    def __init__(self,age=0,name=None,salary=00.00):
        self.age=age
        self.name=name
        self.salary=salary

emp1 = Emp(23)
print(emp1.age,emp1.name,emp1.salary)
emp2=Emp(45,"yadav")
print(emp2.age,emp2.name,emp2.salary)
emp3=Emp(34,"AkarshYadav",8090)
print(emp3.age,emp3.name,emp3.salary,"\n")
print("hii")