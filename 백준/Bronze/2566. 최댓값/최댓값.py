n = 1
m = -1 # 이게 핵심인듯
raw = 0
col = 0
while n <= 9:
    n += 1
    a = list(map(int, input().split()))
    if max(a) > m:
        m = max(a)
        raw = n - 1
        col = a.index(m)+1
print(f"{m}\n{raw} {col}")