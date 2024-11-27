N = int(input())
n = int(str(N)[:])
count = 0
while True:
    if count >= 1 and n == N:
        break
    elif n < 10:
        n = int(str(n)*2)
        count += 1
    else:
        n = int(str(n)[1]+str((int(str(n)[0])+int(str(n)[1]))%10))
        count += 1
print(count)