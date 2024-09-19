T = int(input())
t = 0
while True:
    A, B = map(int, input().split())
    print(A+B)
    t += 1
    if t == T:
        break