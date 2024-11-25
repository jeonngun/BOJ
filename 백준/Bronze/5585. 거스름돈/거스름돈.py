target = 1000 - int(input())
JOI = [500, 100, 50, 10, 5, 1]
count = 0
for i in JOI:
    if target >= i:
        count += target // i
        target %= i
print(count)