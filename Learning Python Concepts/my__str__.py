class Emp:
    def __init__(self):
        self.__age=23
        self.__name='Akash'
        self.__sal=7000
    def show(self):
        print(self.__age,self.__name,self.__sal)

my_list=[10,20,30,40,50]
print(my_list)
my_tuple=(10,20,30,40)
print(my_tuple)
my_dict={"Akash":"python","Arvind":'django'}
print(my_dict)
e=Emp()
e.show()
print("showing a private data")
print(e._Emp__age)
print(e._Emp__name)
print(e._Emp__sal)

print("Printing all instance variable of the class:")
print(dir(e))