N = int(input())
a = input().split()
v = int(input())
if 1 <= N <= 100 and len(a) == N:
    print(a.count(str(v)))