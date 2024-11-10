import sys

N = int(sys.stdin.readline().rstrip())
n = 1
result = set()
while n <= N:
    result.add(int(sys.stdin.readline().rstrip()))
    n += 1
for i in sorted(result):
    print(i)