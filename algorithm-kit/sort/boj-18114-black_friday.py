# https://www.acmicpc.net/problem/18114

from math import comb
from collections import Counter

MAX_VAL = 100_000_001
N, C = map(int, input().split())
weight_list = list(map(int, input().split()))
weight_list.sort()
cnt_list = [0] * MAX_VAL

for weight in weight_list:
    cnt_list[weight] += 1

res = 0
for i, weight_1 in enumerate(weight_list):
    if weight_1 > C:
        break
    elif weight_1 == C:
        res += 1

    for j in range(i + 1, len(weight_list)):
        weight_2 = weight_list[j]
        if weight_1 + weight_2 > C:
            break
        elif weight_1 + weight_2 == C:
            res += 1
        elif (
            C - weight_1 - weight_2 > weight_2 and cnt_list[C - weight_1 - weight_2] > 0
        ):
            res += 1

print(0 if res == 0 else 1)
