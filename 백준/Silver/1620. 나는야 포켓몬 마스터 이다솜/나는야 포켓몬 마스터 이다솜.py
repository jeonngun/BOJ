import sys

N, M = map(int, sys.stdin.readline().split())
book = {}
n, m = 1, 1
while n <= N:
    b = sys.stdin.readline().rstrip()
    book[n] = b
    book[b] = n
    n += 1
while m <= M:
    m += 1
    a = sys.stdin.readline().rstrip()
    if a.isdigit():
        a = int(a)
        print(book[a])
    else:
        print(book[a])