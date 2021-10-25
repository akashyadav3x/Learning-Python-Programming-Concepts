class Emp:
    def __init__(self):
        self.age=45
        self.name='Romit'
        self.sal=56000

    def show(self):
        print(self.age,self.name,self.sal)

    def set_compney(self):
        self.compney='Infosys'

    def set_department(self):
        self.department='IT'

    def delete_intance(self):
        del self.department
        del self.compney

e=Emp()
f=Emp()
print(e.__dict__)
print(f.__dict__)
e.set_compney()
e.set_department()
print(e.__dict__)
print(f.__dict__)
f.set_compney()
f.set_department()
f.delete_intance()
print(e.__dict__)
print(f.__dict__)
