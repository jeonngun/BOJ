X = int(input())
N = int(input())
x,n = 0,0
while True:
    x += eval("*".join(input().split()))
    n += 1
    if n == N:
        break
if x == X:
        print("Yes")
else:
    print("No")