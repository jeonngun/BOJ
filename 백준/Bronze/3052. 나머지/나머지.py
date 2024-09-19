a = []
n = 1
while n <= 10:
    a.append(int(input())%42)
    n += 1
print(len(set(a)))