class Distance:
    def __init__(self,feet,inches):
        self.feet=feet
        self.inches=inches
    def __str__(self):
        return f"feel={self.feet},inches={self.inches}"
    def __add__(self, other):
        feet=self.feet + other.feet
        inches=self.inches + other.inches
        if inches>=12:
            feet=feet + inches//12
            inches= inches%12
        d=Distance(feet,inches)
        return d
obj1=Distance(10,4)
obj2=Distance(12,5)
obj3=obj1 + obj2
print(obj1)
print(obj2)
print("Total feet and inches is:")
print(obj3)