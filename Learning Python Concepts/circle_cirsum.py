class Circle:
    def __init__(self, radius):
        self.radius = radius

    def cal_are(self):
        print("Area of Circle: ", self.radius*self.radius)

    def cal_cum(self):
        print("Circum of Circle: ", (22/7)*2*self.radius)


if __name__ == '__main__':
    radius = int(input("Enter a radius: "))
    ref = Circle(radius)
    ref.cal_are()
    ref.cal_cum()
