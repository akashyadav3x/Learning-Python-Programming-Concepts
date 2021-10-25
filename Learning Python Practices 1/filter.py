def chek_even(x):
    return x % 2 == 0

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(list(filter(chek_even, my_list)))
