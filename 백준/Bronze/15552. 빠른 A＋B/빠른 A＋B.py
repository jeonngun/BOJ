import sys
T = int(sys.stdin.readline())
t = 1
result = []
while t <= T:
    A, B = map(int, sys.stdin.readline().split())
    result.append(A+B)
    t += 1

for i in result:
    print(i)