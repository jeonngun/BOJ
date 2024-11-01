import sys

N = int(sys.stdin.readline())
cards = set(map(int, input().split()))
M = int(sys.stdin.readline())
nums = list(map(int, input().split()))
result = []
for i in nums:
    if i in cards:
        result.append(1)
    else:
        result.append(0)
print(" ".join(list(map(str, result))))