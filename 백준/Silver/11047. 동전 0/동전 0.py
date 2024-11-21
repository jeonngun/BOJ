import sys

N, K = map(int, sys.stdin.readline().split())
n = 1
coins = []
while n <= N:
    coins.append(int(sys.stdin.readline().rstrip()))
    n += 1

result = 0
for i in list(reversed(coins)):
    if K >= i:
        result += (K-(K%i))//i
        K %= i
    elif K == 0:
        break
print(result)