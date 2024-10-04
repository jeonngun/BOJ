T = int(input())
t = 1
while t <= T:
    t += 1
    change = []
    C = int(input())
    for i in [25, 10, 5, 1]:
        change.append(C//i)
        C -= i * (C//i)
    print(" ".join(list(map(str, change))))