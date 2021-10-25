class Student:
    stream='CSE'
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def show_data(self):
        print(self.name,self.roll,self.name)
    #def access_classsvariable(cls):
        #print(Student.stream)
s1=Student('pushp',1)
s2=Student('must',2)
s1.show_data()
s1.stream
s2.show_data()
s2.stream
#del Student.stream
print(s1.__dict__)
print(s2.__dict__)
#Student.access_classsvariable()