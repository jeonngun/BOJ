N = int(input())
Numbers = list(map(int, input().split()))
count = 0
if len(Numbers) == N:
    for i in Numbers:
        if i == 1:
            pass
        elif i == 2:
            count += 1
        else:
            warn = 0
            for j in range(2, i):
                if i % j == 0:
                    warn += 1
            if warn == 0:
                count += 1
    print(count)