S = input()
result = []
a = 0
for i in range(len(S)):
    a += 1
    for j in range(len(S)):
        if a > j:
            try:
                result.append(S[j:a])
            except:
                pass
print(len(set(result)))