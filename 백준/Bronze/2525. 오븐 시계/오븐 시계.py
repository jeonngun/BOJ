A, B = map(int, input().split())
C = int(input())
if (B+C) < 60:
    print(f"{A} {B+C}")
elif (B+C) >= 60:
    if A + (B+C)//60 < 24:
        print(f"{A+(B+C)//60} {(B+C)%60}")
    elif A + B+C//60 >= 24:
        print(f"{A+(B+C)//60-24} {(B+C)%60}")