a, b, c = map(int, input().split())
triangle = []
triangle.append(a)
triangle.append(b)
triangle.append(c)

if len(set(triangle)) == 1:
    print(sum(triangle))
elif max(triangle) < (sum(triangle) - max(triangle)):
    print(sum(triangle))
else:
    print((((a+b+c) - max(a, b, c))*2-1))