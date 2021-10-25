class A:
    def __init__(self):
        self.a=12
        self.b=12
    def __str__(self):
        return f"{self.a,self.b}"
    def __add__(self, other):
        return self.a+self.b+other.a+other.b

class B:
    def __init__(self):
        self.a=12
        self.b=12
    def __str__(self):
        return f"{self.a,self.b}"
    def __add__(self, other):
        return self.a+self.b+other.a+other.b

obj1=A()
obj2=B()
obj3=obj1+obj2
print(obj3)