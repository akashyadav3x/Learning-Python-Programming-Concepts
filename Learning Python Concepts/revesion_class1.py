class Emp:
    #static or class variable
    sex="M"
    def __init__(self,age=0,name='Null',sal=0.0):
        self.age=age
        self.name=name
        self.sal=sal
        #local variable in a method
        var=45
        print(var)

e=Emp(34,'Akash',5000)
f=Emp(56)
g=Emp('name',90000)
print(e.age,e.name,e.sal)
print(f.age,f.name,f.sal)
print(g.age,g.name,g.sal)
print(e.sex)