class Emp:
    def __init__(self):
        self.__age=67
        self.__name="Ankit"
        self.__sal=9000

    def __show(self):
        print(self.__age)
        print(self.__name)
        print(self.__sal)

    def __acces_private_method(self):
        self.__show()

    def private_method(self):
        self.__acces_private_method()


e=Emp()
e.private_method()
print("you are brillant Akash")