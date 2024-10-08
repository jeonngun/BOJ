N, M = map(int, input().split())
n = 1
A = [] # 집합 A 저장
B = [] # 집합 B 저장
result = [] # A+B 저장소
while n <= N: # 시도횟수가 N까지는 집합A의 원소로
    n += 1
    A.append(list(map(int, input().split())))
while n > N: # 시도횟수가 M초과면 집합B의 원소로
    n += 1
    B.append(list(map(int, input().split())))
    if n > (N*2):
        break
#-----------------------------현재 A, B에 원소가 들어있는 상태
for i in range(N):
    save = []
    for j in range(M):
        save.append(A[i][j] + B[i][j])
    result.append(save)
for r in result:
    print(" ".join(list(map(str, r))))