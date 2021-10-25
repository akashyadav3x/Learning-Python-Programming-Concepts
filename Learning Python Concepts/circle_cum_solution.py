import math

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def cal_area(self):
            area=math.pi*math.pow(self.radius,2)
            print("Area of circle is",area)

    def cal_circumference(self):
        circumf=math.tau * self.radius
        print("Circumference of circle is",circumf)

radius=int(input("Enter radius:"))
cobj=Circle(radius)
cobj.cal_area()
cobj.cal_circumference()
