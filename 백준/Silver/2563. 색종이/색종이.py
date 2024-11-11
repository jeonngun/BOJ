N = int(input())
dohwaji = {}
for i in range(1, 101):
    dohwaji[i] = []
    for j in range(100):
        dohwaji[i].append(0)
n = 1
while n <= N:
    X, Y = map(int, input().split())
    for x in range(X, X+10):
        for y in range(Y, Y+10):
            dohwaji[x][y] = 1
    n += 1

result = 0
for k in range(1, 101):
    result += dohwaji[k].count(1)

print(result)