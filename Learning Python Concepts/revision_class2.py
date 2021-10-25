class Student:
    sex = 'M'
    def __init__(self,age,name,grade):
        self.age=age
        self.name=name
        self.grade=grade
    def show(self):
        self.per=89
        print(self.age,self.name,self.grade,self.sex,self.per)
s1=Student(24,'Akash',"a")
print(s1.__dict__)
s1.show()
print(s1.__dict__)
s1.__dict__['department']='IT'
print(s1.__dict__)
s1.you="kamina"
print(s1.__dict__)