import sys

N = int(sys.stdin.readline().rstrip())
nums = []
n = 1
while n <= N:
    nums.append(int(sys.stdin.readline().rstrip()))
    n += 1

first = round(sum(nums)/N)
second = sorted(nums)[N//2]
c = {}
for i in set(nums):
    c[i] = 0
for num in nums:
    c[num] += 1

ck = list(c.keys())
cv = list(c.values())

bin = []
if cv.count(max(cv)) >= 2:
    for j in ck:
        if c[j] == max(cv):
            bin.append(j)
    bin.remove(min(bin))
    third = min(bin)


else:
    ind = cv.index(max(cv))
    third = ck[ind]

forth = max(nums) - min(nums)

print(first)
print(second)
print(third)
print(forth)