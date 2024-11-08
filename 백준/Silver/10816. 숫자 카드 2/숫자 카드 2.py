import sys

N = int(sys.stdin.readline())
sg = sys.stdin.readline().split()
SG = {}
for i in set(sg):
    SG[i] = 0
for j in sg:
    SG[j] += 1
M = int(sys.stdin.readline())
cards = sys.stdin.readline().split()

for k in cards:
    try:
        print(SG[k], end=' ')
    except:
        print(0, end=' ')