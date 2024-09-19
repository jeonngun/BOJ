N = int(input())
a = input()
A = a.split()
if len(a.split()) == N and 1 <= N <= 1000000:
    print(f"{min(map(int, A))} {max(map(int, A))}")