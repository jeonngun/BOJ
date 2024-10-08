N = int(input())
n = 1
A = []
while n <= N:
    n += 1
    A.append(input())
A = sorted(list(set(A)))
result = {}
for i in range(1, max(list(map(len, A)))+1):
    result[i] = []
    for j in A:
        if i == len(j):
            result[i].append(j)
for k in range(1, len(result)+1):
    for l in range(max(list(map(len, result.values())))):
        try:
            print(result[k][l])
        except:
            pass