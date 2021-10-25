import math


class Circle:
    def __init__(self, r):
        self.radius = r

    def cal_area(self):
        area = math.pi * math.pow(self.radius, 2)
        print("Area is : ", area)

    def cal_cir(self):
        cir = math.tau * self.radius
        print("cir of circle : ", cir)


radius = int(input("Enter radius: "))

obj = Circle(radius)
obj.cal_area()
obj.cal_cir()
