d = {}
for _ in range(int(input())):
    name = input()
    score = float(input())
    d[name] = score

values = d.values()
second = sorted(list(set(values)))[1]
second_lowest = []
for key, value in d.items():
    if value == second:
        second_lowest.append(key)
print(d)
