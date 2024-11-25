S = int(input())
result = 0
count = 0
for i in range(1, S+1):
    if S == 2:
        count = 1
    elif result == S:
        break
    elif result > S:
        count -= 1
        break
    else:
        result += i
        count += 1

print(count)