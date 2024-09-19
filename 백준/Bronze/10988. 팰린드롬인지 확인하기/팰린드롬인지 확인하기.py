a = input().lower()
be_pal = "".join(list(reversed(list(a))))
if a == be_pal:
    print("1")
else:
    print("0")