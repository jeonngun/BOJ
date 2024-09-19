a = []
n = 1
while n <= 28:
    a.append(int(input()))
    n += 1
for i in range(1, 31):
    try:
        a.index(i)
    except:
        print(i)