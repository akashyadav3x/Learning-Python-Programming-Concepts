class Emp:
    raise_amount=7.5
    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self.sal=sal
    def increse_sal(self):
        self.sal=self.sal+(self.sal * Emp.raise_amount/100)
    def display(self):
        print(self.age,self.name,self.sal)
    def __str__(self):
        return f"Salary is:{self.sal}"

emp1=Emp(24,'Ram',6000)
emp2=Emp(25,'Hariya',8000)
print("Before incremanting the salary:")
print(emp1)
print(emp2)
emp1.increse_sal()
#Emp.increse_sal()
print("After incremanting the salary:")
print(emp1)
print(emp2)