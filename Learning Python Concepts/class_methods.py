class Car:
    @classmethod
    def myclass(cls):
        cls.var='I Am fine'
        print("i Am in class method")
    def __init__(self,color,price):
        self.color=color
        self.price=price
    def show(self):
        print(self.color,self.price)

c=Car('biue',60000)
c.show()
Car.myclass()
print(Car.var)