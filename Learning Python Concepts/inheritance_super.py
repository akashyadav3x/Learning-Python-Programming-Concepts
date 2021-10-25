class Emp:
    def __init__(self,age,name,sal):
        self.age=age
        self.name=name
        self.sal=sal
class UseEmp(Emp):
    def __init__(self,sex):
        self.sex=sex
        Emp.__init__(self,45,'Akash',5600)
    def call_using_super(self):
        super().__init__(34,'Kailesh',890)
    def __str__(self):
        return f"{self.age,self.name,self.sal,self.sex}"

e=UseEmp('M')
print(e)
e.call_using_super()
print(e)