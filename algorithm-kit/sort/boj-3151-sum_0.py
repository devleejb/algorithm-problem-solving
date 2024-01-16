# https://www.acmicpc.net/problem/3151

from sys import stdin
from collections import Counter
from math import comb

input = stdin.readline

ARR_MAX = 20_001
OFFSET = 10_000

N = int(input())
a_list = list(map(int, input().split()))
cnt_list = [0] * ARR_MAX

for a in a_list:
    cnt_list[a + OFFSET] += 1
res = 0

for i in range(ARR_MAX):
    start_num = i - OFFSET

    if cnt_list[i] == 0:
        continue

    for j in range(i, ARR_MAX):
        mid_num = j - OFFSET
        end_num = -start_num - mid_num

        if mid_num > end_num:
            break

        if (
            -OFFSET <= end_num <= OFFSET
            and cnt_list[j] > 0
            and cnt_list[end_num + OFFSET] > 0
        ):
            common_list = Counter([i, j, end_num + OFFSET]).most_common()
            tmp = 1
            for num, cnt in common_list:
                tmp *= comb(cnt_list[num], cnt)
            res += tmp

print(res)
