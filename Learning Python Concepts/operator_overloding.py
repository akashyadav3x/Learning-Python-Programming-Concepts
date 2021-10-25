class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return f"{self.a,self.b}"
    def __add__(self, other):
        return (self.a+self.b)+(other.a+other.b)

obj1=A(11,1)
obj2=A(12,1)
obj3=A(12,2)
obj4 = obj1 + obj2 + obj3
print(obj4)