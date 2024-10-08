n = 1
result = []
while n <= 5:
    n += 1
    result.append(int(input()))
print(int(sum(result)/len(result)))
print(sorted(result)[2])