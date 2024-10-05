N = int(input())
doom = []
for i in range(1, 2666800):
    if "666" in str(i):
        doom.append(int(i))
print(doom[N-1])