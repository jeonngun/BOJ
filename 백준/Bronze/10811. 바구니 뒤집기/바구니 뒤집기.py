N, M = map(int, input().split())
#------------바구니 생성------------
b = []
for c in range(1, N+1):
    b.append(c)
#----------------------------------
m = 1 # M 시도횟수 카운트
while m <= M:
    m += 1
    i, j = map(int, input().split())
    left = [] # 좌변
    right = [] # 우변
    change = [] # 순서 바꾸기(중앙)
    for l in b[:i-1]:
        left.append(l)
    for r in b[j:]:
        right.append(r)
    for h in range(j-1, i-2, -1):
        change.append(b[h])    
    b = left + change + right #(좌변 + 순서 바꾸기(중앙) + 우변)
print(" ".join(map(str, b))) #예시대로 정수 사이에 공백 넣어 출력