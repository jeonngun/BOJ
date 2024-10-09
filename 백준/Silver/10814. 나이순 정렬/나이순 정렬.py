N = int(input())
n = 1
members = []
while n <= N:
    n += 1
    age, name = map(str, input().split())
    members.append([int(age), n-1, name])
for i in sorted(members):
    print(f"{i[0]} {i[2]}")