class Person:
    def __init__(self,age,name):
        self.__age=age
        self.__name=name
    def get_age(self):
        return self.__age
    def get_name(self):
        return self.__name
class Student:
    def __init__(self,roll,marks):
        self.__roll=roll
        self.__marks=marks
    def get_roll(self):
        return self.__roll
    def get_marks(self):
        return self.__marks
class DrivedClass(Person,Student):
    def __init__(self,age,name,roll,marks,strem):
        Person.__init__(self,age,name)
        Student.__init__(self,roll,marks)
        self.__strem=strem
    def get_stream(self):
        return self.__strem

d = DrivedClass(24,'akarsh',101,56.78,'CSE',)
print(d.get_age())
print(d.get_name())
print(d.get_roll())
print(d.get_marks())
print(d.get_stream())
print(Student.mro())
print(Person.mro())
print(DrivedClass.mro())