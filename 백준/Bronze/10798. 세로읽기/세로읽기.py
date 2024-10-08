n = 1
ys = {}
for i in range(1, 16):
    ys[i] = []

while n <= 5:
    n += 1
    a = input()
    for j in range(1, len(a)+1):
        try:
            ys[j].append(a[j-1])
        except:
            pass
        
result = []
for k in list(ys.values()):
    result.append("".join(k))

print("".join(result))