a = input()
b = list(map(int, a.split(" ")))
A, B, C = b[0], b[1], b[2]
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)