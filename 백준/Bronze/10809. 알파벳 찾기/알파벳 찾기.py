S = input().lower()
for i in range(97, 123):
    print(f"{S.find(chr(i))}", end=' ')