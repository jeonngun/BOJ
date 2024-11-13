import sys

N = int(sys.stdin.readline().rstrip())
n = 6
result = 1
r = set()
while result <= N:
    r.add(result)
    result += n
    n += 6
if N > max(r):
    print(len(r)+1)
else:
    print(len(r))