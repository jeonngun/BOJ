N = int(input())
n = 2
result = []
while True:
    if N == 1:
        break
    elif N % n == 0:
        result.append(n)
        N = N // n
    else:
        n += 1
for i in result:
    print(i)