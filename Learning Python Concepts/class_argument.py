class Emp:
    def __init__(self,x,y,z):
        self.age=x
        self.name=y
        self.salary=z

my_emp1 = Emp(23,"Akash",5000)
print("Age is:",my_emp1.age,"Name is:",my_emp1.name,"Salary is:",my_emp1.salary)
my_emp2 = Emp(67,'Muskan',89000)
print("age is:",my_emp2.age,"Name is:",my_emp2.name,"Salary is:",my_emp2.salary)
my_emp3 = Emp(55.09,'love',98000)
print("age is:",my_emp3.age,"Name is:",my_emp3.name,"Salary is:",my_emp3.salary)