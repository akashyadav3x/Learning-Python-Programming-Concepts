filename = input("Enter a file name ")
file = open(filename, 'r')
data = file.read()
print(data.upper())
