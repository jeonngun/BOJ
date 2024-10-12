x, y = [], []
n = 1
while n <= 3:
    point = list(map(int, input().split()))
    x.append(point[0])
    y.append(point[1])
    n += 1
setx = set(x)
sety = set(y)

result = []
for sx in setx:
    if x.count(sx) % 2 == 1:
        result.append(sx)
for sy in sety:
    if y.count(sy) % 2 == 1:
        result.append(sy)

print(" ".join(list(map(str, result))))