N, M = map(int, input().split())
nums = list(map(int, input().split()))
result = 0
if N == len(nums):
    for x in nums:
        for y in nums:
            for z in nums:
                if x != y and y != z and x != z and (M-result) >= (M-(x+y+z)) >= 0:
                    result = (x+y+z)
print(result)