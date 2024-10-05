N = int(input())
result = []
result2 = []
for i in range(3, (N - (N % 3) + 1), 3):
    if N == i:
        result.append((i, 0))
    else:
        for j in range(5, (N - (N % 5) + 1), 5):
            if N == i+j:
                result.append((i, j))
            elif N == j:
                result.append((0, j))
try:
    for a in result:
        result2.append(a[0]//3 + a[-1]//5)
    print(min(result2))
except:
    print("-1")