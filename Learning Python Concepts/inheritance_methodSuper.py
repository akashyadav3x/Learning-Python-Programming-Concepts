class person(object):
    def __init__(self,age,name):
        self.__age=age
        self.__name=name
    def __str__(self):
        return f"Age is:{self.__age},Name is:{self.__name}"

class Emp(person):
    def __init__(self,age,name,id,sal):
        super().__init__(age,name)
        self.__id=id
        self.__sal=sal
    def __str__(self):
        str=super().__str__()
        return f"{str},Id is:{self.__id},salry is:{self.__sal}"


e=Emp(67,'Akash',101,9000)
print(e)