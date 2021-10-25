class point:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return f"a={self.a},b={self.b}"
    def __add__(self, other):
        a=self.a+other.a
        b=self.b+other.b
        p=point(a,b)
        return p

obj1=point(1,2)
obj2=point(1,3)
obj4=obj1 + obj2
print(obj4)
obj=obj1 + obj2 + obj4
print(obj)