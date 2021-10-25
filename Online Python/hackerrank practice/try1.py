
if __name__ == '__main__':
    n = int(input())
    s = 0
    p = 0
    i = 0
    while i != n:
        i += 1
        x = int(input())
        if x > s:
            p = s
            s = x

    print("high ", s)
    print('low ', p)
