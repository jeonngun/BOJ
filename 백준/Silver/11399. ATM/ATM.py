N = int(input())
P = list(map(int, input().split()))

result = 0
n = 0
for i in sorted(P):
    n += i
    result += n

print(result)