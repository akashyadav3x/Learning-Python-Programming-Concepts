class Human:
    def __init__(self,age,name,occpation):
        self.__age=age
        self.__name=name
        self.__occupation=occpation

    def work(self):
        if(self.__occupation == "student"):
            return(f"{self.__name} is studing in collage")
        else:
            return(f"{self.__name} is an employee")

    def eat(self):
        return(f"{self.__name} is eating")

    def talk(self):
        return(f"{self.__name} is talking")

    def __str__(self):
        a = self.eat()
        b = self.talk()
        c = self.work()
        return f"{a}\n{b}\n{c}"

Akash = Human(18, "Akash", "student")
Muskan = Human(17, "Muski", "student")
Pankaj = Human(45, "Pankaj", "Profeccer")
print(Akash)
print(Muskan)
print(Pankaj)