T = int(input())
n = 1
while n <= T:
    result = []
    R, S = input().split()
    for i in range(len(S)):
        result.append(int(R) *S[i])
    print("".join(result))
    n += 1