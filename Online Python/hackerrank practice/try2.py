'''
n = int(input())

nums = map(int, input().split())
print(sorted(list(set(nums)))[-2])
'''
a = int(input())
num = map(int, input().split())
x = sorted(set(num))
x = list(x)
print(x[-2])
