A, B = map(str, input().split())
SA = int("".join(list(reversed(list(A)))))
SB = int("".join(list(reversed(list(B)))))
print(max(SA, SB))