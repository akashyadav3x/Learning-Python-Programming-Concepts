def fact(n):
    f = 1
    while n > 1:
        f = f * n
        n -= 1
    return f


if __name__ == '__main__':
    a = int(input("ENter a no: "))
    fact = fact(a)
    print("factoeial is: ", fact)
