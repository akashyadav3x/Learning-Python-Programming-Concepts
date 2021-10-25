class Student:
    def __init__(self):
        self.__name="Akash"
        self.__age=78
        self.__per=78.78

    def __str__(self):
        return  f"name is:{self.__age},\nname is:{self.__name},\nPer is:{self.__per}"

S=Student()
print(S)