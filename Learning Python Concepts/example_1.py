
class Akash:
    def __init__(self):
        self.__Age=29
        self.__Name="Akash"
        self.__sal=9000

    def __str__(self):
        #return str(self.__Age)+" "+str(self.__Name)+" "+str(self.__sal)
        return f"age is:{self.__Age},\nName is:{self.__Name},\nSalary is:{self.__sal}"

ak=Akash()
print(ak)
print(dir(ak))