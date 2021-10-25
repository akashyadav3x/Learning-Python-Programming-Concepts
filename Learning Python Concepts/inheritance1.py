class Animal:
    def eat(self):
        print("it is eating")
    def sleep(self):
        print("It is sleeping")

class Bird(Animal):
    def set_type(self,type):
        self.type=type
    def flay(self):
        print("It can be flay")
    def __str__(self):
        return f"It is :{type}"

obj=Bird()
obj.set_type("Duck")
print(obj)
obj.flay()
obj.sleep()
obj.eat()