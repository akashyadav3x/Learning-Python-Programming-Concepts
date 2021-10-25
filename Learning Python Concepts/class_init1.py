class Student:
    def __init__(my_self):
        my_self.age=25
        my_self.name="Akash Yadav"
        my_self.salery=80000
        my_self.__sal=78009

student=Student()
student.gender='m'
my_student=Student()
print(student.age,student.name,student.salery)
print(my_student.age,my_student.name,my_student.salery)
print(student.age,student.name,student.salery,student.gender)
student.__dict__['__sal']=678
print(student.__dict__)
print(student.__sal)
print(student.__sal)