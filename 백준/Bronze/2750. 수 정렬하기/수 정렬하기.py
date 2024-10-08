N = int(input())
n = 1
save =[]
while n <= N:
    n += 1
    save.append(int(input()))
for i in sorted(save):
    print(i)