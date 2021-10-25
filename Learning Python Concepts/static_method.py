class Akash:
    @staticmethod
    def Display():
        print("My name is Akash Yadav")
    @classmethod
    def Display(cls):
        print("My name is Nitesh Yadav")
    def Display(self):
        print("This is a instance method")

a=Akash()
a.Display()