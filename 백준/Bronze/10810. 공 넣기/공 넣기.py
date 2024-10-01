N, M = map(int, input().split())
# N = 바구니 개수 M = 공 넣기 트라이 수
m = 1 # 공 시도 카운트
n = 1 # 바구니 생성?
b = {1:0}
while n < N:
    n += 1
    b[n] = 0
while m <= M:
   m += 1
   i, j, k = map(int, input().split())
   for trial in range(i, j+1):
       b[trial] = k
print(" ".join(map(str, b.values())))