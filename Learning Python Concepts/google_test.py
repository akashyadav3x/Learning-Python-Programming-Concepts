'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
my_input = int(input())
i = 1
while (i <= my_input):
    n = int(input())
    x = int(input())
    y = int(input())
    if (n == 1):
        for i in range(1, 10):
            if (i % x == 0 and i % y == 0):
                print(i)

    elif (n == 2):
        for i in range(10, 100):
            if (i % x == 0 and i % y == 0):
                print(i)

    elif (n == 3):
        for i in range(100, 1000):
            if (i % x == 0 and i % y == 0):
                print(i)

    elif (n == 4):
        for i in range(1000, 10000):
            if (i % x == 0 and i % y == 0):
                print(i)

    elif (n == 5):
        for i in range(10000, 100000):
            if (i % x == 0 and i % y == 0):
                print(i)

    elif (n == 6):
        for i in range(100000, 1000000):
            if (i % x == 0 and i % y == 0):
                print(i)

    if (n == 7):
        for i in range(1000000, 10000000):
            if (i % x == 0 and i % y == 0):
                print(i)

    if (n == 8):
        for i in range(10000000, 100000000):
            if (i % x == 0 and i % y == 0):
                print(i)

    elif (n == 9):
        for i in range(100000000, 1000000000):
            if (i % x == 0 and i % y == 0):
                print(i)

    elif (n == 10):
        for i in range(1000000000, 10000000000):
            if (i % x == 0 and i % y == 0):
                print(i)

    i = i + 1