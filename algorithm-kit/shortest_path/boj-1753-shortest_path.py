# https://www.acmicpc.net/problem/1753
from sys import stdin, maxsize
import heapq

input = stdin.readline

V, E = map(int, input().split())
K = int(input())
edges = [[] for _ in range(V)]
costs = [maxsize for _ in range(V)]
visited = [False for _ in range(V)]

for _ in range(E):
    start, end, cost = map(int, input().split())
    start -= 1
    end -= 1
    edges[start].append((end, cost))

heap = []
costs[K - 1] = 0
heapq.heappush(heap, (0, K - 1))

while heap:
    (cost, node) = heapq.heappop(heap)

    if visited[node]:
        continue

    visited[node] = True

    for end, edge_cost in edges[node]:
        costs[end] = min(costs[end], cost + edge_cost)
        heapq.heappush(heap, (costs[end], end))

for cost in costs:
    if cost == maxsize:
        print("INF")
    else:
        print(cost)
