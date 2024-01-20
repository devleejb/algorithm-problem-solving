# https://www.acmicpc.net/problem/1202
from sys import stdin
import heapq
import bisect

input = stdin.readline

N, K = map(int, input().split())
jewerly_list = [list(map(int, input().split())) for _ in range(N)]
bag_list = [int(input()) for _ in range(K)]

jewerly_list.sort()
bag_list.sort()

pq = []
idx_in_heap = 0
res = 0

for bag in bag_list:
    right_idx = bisect.bisect_right(jewerly_list, [bag, 1_000_001])
    for i in range(idx_in_heap, right_idx):
        heapq.heappush(pq, -jewerly_list[i][1])
    idx_in_heap = right_idx

    if len(pq) > 0:
        res += heapq.heappop(pq)

print(-res)
