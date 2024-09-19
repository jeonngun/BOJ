H, M = map(int, input().split())
if M >= 45:
    print(f"{H} {M-45}")
elif H >= 1 and M < 45:
    print(f"{H-1} {60+(M-45)}")
elif H < 1 and M < 45:
    print(f"{24+(H-1)} {60+(M-45)}")