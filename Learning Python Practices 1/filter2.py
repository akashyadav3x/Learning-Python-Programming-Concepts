def f1(num):
    if num % 2 == 0:
        return num


mynums = [1, 2, 3, 4, 5, 6]
print(list(filter(f1, mynums)))
