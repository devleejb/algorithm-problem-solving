from sys import stdin
from bisect import bisect_left

input = stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
sum_nums = []
subtract_nums = []


for i in range(N):
    for j in range(N):
        max_val = max(nums[i], nums[j])
        sum_nums.append(nums[i] + nums[j])
        subtract_nums.append((max_val, abs(nums[i] - nums[j])))

sum_nums.sort()
subtract_nums.sort(key=lambda n: -n[0])

res = 0

for max_val, target_sum in subtract_nums:
    idx = bisect_left(sum_nums, target_sum)

    if sum_nums[idx] == target_sum:
        res = max_val
        break

print(res)
