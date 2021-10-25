count = 0
total = 0

while True:
    inp = input("Enter a no (done for exit) ")
    if inp == 'done':
        break
    total += float(inp)
    count += 1

varage = total/count
print("avrage is: ", varage)
