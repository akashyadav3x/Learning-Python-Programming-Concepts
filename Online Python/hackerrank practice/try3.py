if __name__ == '__main__':
    mylist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        mylist.append([name, score])


mylist.sort()
print(mylist)
