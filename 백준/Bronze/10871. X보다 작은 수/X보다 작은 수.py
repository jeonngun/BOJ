N, X = map(int, input().split())
A = input()
for i in A.split():
    if int(i) < X:
        print(i, end=' ')