class Emp:
    def __init__(self):
        print("Counstrutor is called")

    def __str__(self):
        print("Hello python")
        return "You are grate"

    def __del__(self):
        print("Destructor is called:")

t=e=Emp()
e=t
del t
print("Hii")
print(e)
del e
print("hyyy")