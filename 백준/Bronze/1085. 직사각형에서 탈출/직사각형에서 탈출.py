x, y, w, h = map(int, input().split())
compare = []
compare.append(w-x)
compare.append(abs(0-x))
compare.append(h-y)
compare.append(abs(0-y))
print(min(compare))