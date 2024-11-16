X = int(input())
row = [1]
n = 1
for i in range(1, X+1):
    n += i
    row.append(n)
    if n > X:
        row.remove(max(row))
        break

start = len(row)
index = X - max(row)

if start % 2 == 0:
    print(f'{1+index}/{start-index}')
else:
    print(f'{start-index}/{1+index}')