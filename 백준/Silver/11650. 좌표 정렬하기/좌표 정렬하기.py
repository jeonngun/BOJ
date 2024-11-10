import sys

N = int(sys.stdin.readline().rstrip())
n = 1
result = []
while n <= N:
    A, B = map(int, sys.stdin.readline().split())
    result.append((A, B))
    n += 1
for a, b in sorted(result):
    print(f'{a} {b}')