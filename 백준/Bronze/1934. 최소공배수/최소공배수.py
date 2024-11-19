import sys

T = int(sys.stdin.readline().rstrip())
t = 1
result = []
while t <= T:
    A, B = map(int, sys.stdin.readline().split())
    n = 1
    for i in range(max(A, B), 1, -1):
        if A % i == 0 and B % i == 0:
            A, B = A//i, B//i
            n *= i
    result.append(A*B*n)
    t += 1

for _ in result:
    print(_)