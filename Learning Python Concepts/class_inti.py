'''
class Test:
    print("Hello python")
    def __init__(self):
        print("Python is a genral perpost programming ")
        print("Address of thr self",self)
    
ref = Test()
print(ref)
'''

class Student:
    def __init__(self,age,name,salary):
        self.age=age
        self.name=name
        self.salary=salary

student=Student(24,'Akash Yadav',30000)
print("Age is:",student.age,"\nName is:",student.name,"\nSalary is:",student.salary)
student.grade='M'
print(student.grade)