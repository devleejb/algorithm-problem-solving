# https://www.acmicpc.net/problem/7662
from sys import stdin
import heapq

input = stdin.readline

T = int(input())
res_list = []

for i in range(T):
    K = int(input())
    max_heap, min_heap = [], []
    nums = {}
    for k in range(K):
        op, num = input().split()
        num = int(num)
        if op == "I":
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)
            if nums.get(num) is not None:
                nums[num] += 1
            else:
                nums[num] = 1
        elif len(nums) > 0:
            deleted = False

            while not deleted:
                deleted_num = 0
                if num == -1:
                    deleted_num = heapq.heappop(min_heap)
                else:
                    deleted_num = -heapq.heappop(max_heap)

                if nums.get(deleted_num) is not None and nums[deleted_num] > 0:
                    nums[deleted_num] -= 1
                    deleted = True

                    if nums.get(deleted_num) == 0:
                        del nums[deleted_num]
    if len(nums) == 0:
        res_list.append(["EMPTY"])
    else:
        sorted_keys = sorted(nums.keys())
        res_list.append([sorted_keys[len(sorted_keys) - 1], sorted_keys[0]])

for res in res_list:
    print(*res)
