# https://www.acmicpc.net/problem/1016
from sys import stdin
from math import sqrt, floor, ceil

input = stdin.readline

min_val, max_val = map(int, input().split())
is_no_squared_num = [True] * (floor(sqrt(max_val)) + 1)
res = max_val - min_val + 1
is_no_squared_num_in_target = [True] * res

for i in range(2, floor(sqrt(max_val)) + 1):
    if not is_no_squared_num[i]:
        continue

    squared_num = i ** 2
    j = 1

    while squared_num * j <= floor(sqrt(max_val)):
        is_no_squared_num[squared_num * j] = False
        j += 1

    for j in range(max(ceil(min_val / squared_num), 1), floor(max_val / squared_num) + 1):
        if not is_no_squared_num_in_target[squared_num * j - min_val]:
            continue
        
        is_no_squared_num_in_target[squared_num * j - min_val] = False
        res -= 1

print(res)