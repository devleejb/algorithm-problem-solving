# https://www.acmicpc.net/problem/2461
from sys import stdin, maxsize
import heapq

input = stdin.readline


N, M = map(int, input().split())
stats = [sorted(list(map(int, input().split()))) for _ in range(N)]
pointers = [0] * N
res = maxsize
heap = []
max_val = 0

for i in range(N):
    heapq.heappush(heap, (stats[i][0], i))
    max_val = max(max_val, stats[i][0])

while heap:
    stat, class_num = heapq.heappop(heap)
    res = min(res, max_val - stat)

    if pointers[class_num] == M:
        break

    heapq.heappush(heap, (stats[class_num][pointers[class_num]], class_num))
    max_val = max(max_val, stats[class_num][pointers[class_num]])
    pointers[class_num] += 1


print(res)
