N = int(input())
result = []
for M in range(N):
    if N == M + sum(list(map(int, str(M)))):
        result.append(M)
if len(result) == 0:
    print("0")
else:
    print(min(result))