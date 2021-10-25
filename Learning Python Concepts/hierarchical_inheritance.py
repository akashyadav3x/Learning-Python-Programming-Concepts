class School_members(object):
    def __init__(self,age,name):
        self.__age=age
        self.__name=name
        print("School members constructor is called")
    def tell(self):
        return f"Age is:{self.__age}, Name is:{self.__name}"

class Teacher(School_members):
    def __init__(self,age,name,sal):
        super().__init__(age,name)
        self.__sal=sal
        print("Techar constructor is called")
    def tell(self):
        return f"{super().tell()}, Salary is:{self.__sal}"

class Student(School_members):
    def __init__(self,age,name,marks):
        super().__init__(age,name)
        self.__marks=marks
        print("Student constructor is called")
    def tell(self):
        return f"{super().tell()}, Marks is:{self.__marks}"

class Players(School_members):
    def __init__(self,age,name,run):
        super().__init__(age,name)
        self.__run=run
    def tell(self):
        return f"{super().tell()}, Run is:{self.__run}"
s = Student(14,'Akarsh',56.78)
print(s.tell())
print("==================================")
t = Teacher(56,"Tejashvani mourys",60000)
print(t.tell())
print("=====================================")
p = Players(34,'Virat kholi',787)
print(p.tell())
members=[t,p]
for contant in members:
    print(contant.tell())
print(issubclass(Student,School_members))
print(issubclass(Teacher,School_members))
print(issubclass(School_members,object))