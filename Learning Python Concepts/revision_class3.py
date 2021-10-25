class Emp:
    def __init__(self,age,name,sal):
        self.age=age
        self.name=name
        self.sal=sal

    def set_compney(self):
        self.compney='Infosis'

    def set_department(self):
        self.department='Security'

e=Emp(23,'Akash',56000)
f=Emp(45,'Kailesh',89000)
e.set_compney()
e.set_department()
print(e.age,e.name,e.sal,e.department,e.compney)
print(f.age,f.name,f.sal)
print(e.__dict__)
print(f.__dict__)