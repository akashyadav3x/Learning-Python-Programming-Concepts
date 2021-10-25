class myClass:
    value1=10
    value2=99
    def __init__(self):
        self.name='Akash'
    def add_value(self):
        myClass.value2=20
    def overwrite_value(self):
        myClass.value=90
    def class_method(self):
        del myClass.value1

print(myClass.__dict__)
obj=myClass()
obj.add_value()
print(myClass.__dict__)
print(obj.__dict__)
obj.overwrite_value()
print(myClass.__dict__)
obj.class_method()
print(myClass.value2)
#print(myClass.value1)
print(myClass.__dict__)