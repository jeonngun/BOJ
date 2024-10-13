N = int(input())
n = 1
x, y = [], []
while n <= N:
    X, Y = map(int, input().split())
    x.append(X)
    y.append(Y)
    n += 1
print(((max(x)-min(x))*(max(y)-min(y))))