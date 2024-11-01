N = int(input())
n = 0
while n <= N:
    result = ((2**n)+1)**2 # 첫번째 줄의 변의 개수만 놓고 생각해보니 2의 제곱 규칙을 발견...
    n += 1
print(result)