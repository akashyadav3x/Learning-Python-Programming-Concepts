class Emp:
    @classmethod
    def raise_amount(cls,persantage):
        cls.raise_amount=persantage
    def __init__(self,age,name,sal):
        self.age=age
        self.name=name
        self.sal=sal
    def show(self):
        print("salary of ",self.name,"is ",self.sal)
    def incress_sal(self):
        self.sal=self.sal + (Emp.raise_amount * self.sal)/100

e=Emp(45,'kavita',50000)
f=Emp(67,'Savita',45000)
val=float(input("Enter a raise persantages: "))
Emp.raise_amount(val)
print("--------------------------------------")
print("Before incremanting ")
e.show()
f.show()
print("---------------------------------------")
print("After incremanting by ",val)
e.incress_sal()
f.incress_sal()
e.show()
f.show()
