M = int(input())
N = int(input())
result = []
for i in range(M, N+1):
    n = 0
    for x in range(2, i):
        if i % x == 0:
            n += 1
    if n == 0 and i > 1:
        result.append(i)
if len(result) == 0:
    print('-1')
else:
    print(sum(result))
    print(min(result))