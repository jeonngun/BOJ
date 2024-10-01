N, M = map(int, input().split())
b = {} # 바구니 생성
# 바구니 초기 세팅 -----------
for c in range(1, N+1):
    b[c] = c
# ---------------------------
m = 1
while m <= M:
    i, j = map(int, input().split())
    b[i], b[j] = b[j], b[i]
    m += 1
print(" ".join(map(str, b.values())))