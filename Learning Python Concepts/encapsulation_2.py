class Emp:
    def __init__(self,age,name,sal):
        self.__age=age
        self.__name=name
        self.__sal=sal

    def show(self):
        print(self.__age,self.__name,self.__sal)

e=Emp(25,"Ankit",5000)
e.show()