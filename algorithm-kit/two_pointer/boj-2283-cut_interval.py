# https://www.acmicpc.net/problem/2283
from sys import stdin

input = stdin.readline

MAX_LENGTH = 1_000_001
N, K = map(int, input().split())
intervals = [list(map(int, input().split())) for _ in range(N)]
interval_sums = [0] * 1_000_001
max_pos = 0

for interval in intervals:
    start, end = interval
    max_pos = max(max_pos, end)
    for i in range(start, end):
        interval_sums[i] += 1

for i, interval_sum in enumerate(interval_sums):
    if i == 0:
        continue
    interval_sums[i] = interval_sums[i - 1] + interval_sum

i, j = 0, 1
found = False

while i <= max_pos and j <= max_pos:
    length_sum = interval_sums[j - 1] - (0 if i == 0 else interval_sums[i - 1])

    if length_sum == K:
        found = True
        break

    if length_sum > K:
        i += 1
    else:
        j += 1

if found:
    print(i, j)
else:
    print(0, 0)
