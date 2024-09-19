N, K = map(int, input().split())
t = 0
for i in range(1, N+1):
    if N % i == 0:
        t += 1
        if t == K:
            print(i)
if t < K:
    print('0')