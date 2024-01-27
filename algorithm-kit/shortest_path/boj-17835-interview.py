# https://www.acmicpc.net/problem/17835
from sys import stdin, maxsize
import heapq

input = stdin.readline

N, M, K = map(int, input().split())
edges = [[] for _ in range(N)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    start -= 1
    end -= 1
    edges[end].append((start, cost))

interview_city_list = list(map(int, input().split()))


cost_list = [maxsize for _ in range(N)]
visited_list = [False for _ in range(N)]
heap = []

for interview_city in interview_city_list:
    interview_city -= 1
    heapq.heappush(heap, (0, interview_city))
    cost_list[interview_city] = 0

while heap:
    distance, city = heapq.heappop(heap)

    if visited_list[city]:
        continue

    visited_list[city] = True

    for to_city, cost in edges[city]:
        next_distance = cost + distance

        if cost_list[to_city] == -1 or next_distance < cost_list[to_city]:
            cost_list[to_city] = next_distance
            heapq.heappush(heap, (next_distance, to_city))

res = max(enumerate(cost_list), key=lambda c: (c[1], -c[0]))
print(res[0] + 1)
print(res[1])
