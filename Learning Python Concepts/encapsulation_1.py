class Emp:
    def __init__(self):
        self.age=23
        self.name="Ramesh"
        self.__sal=50000

    def show(self):
        print(self.age,self.name,self.__sal)

e=Emp()
print("Hello python")
e.show()
print(e.age)
print(e.name)
print(e.__sal)