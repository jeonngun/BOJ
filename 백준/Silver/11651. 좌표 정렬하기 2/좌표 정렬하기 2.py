import sys

N = int(sys.stdin.readline().rstrip())
n = 1
result = []
while n <= N:
    x, y = map(int, sys.stdin.readline().split())
    result.append((y, x))
    n += 1
for y, x in sorted(result):
    print(f'{x} {y}')