# https://www.acmicpc.net/problem/11779
from sys import stdin, maxsize
import heapq

input = stdin.readline

n = int(input())
m = int(input())
edges = [[] for _ in range(n)]
costs = [maxsize for _ in range(n)]
visited = [False for _ in range(n)]
prev_city = [-1 for _ in range(n)]
heap = []

for _ in range(m):
    start, end, cost = map(int, input().split())
    start -= 1
    end -= 1
    edges[start].append((end, cost))

start, end = map(int, input().split())
start -= 1
end -= 1
costs[start] = 0
prev_city[start] = start
heapq.heappush(heap, (0, start))

while heap:
    distance, from_city = heapq.heappop(heap)

    if visited[from_city]:
        continue

    visited[from_city] = True

    for to_city, cost in edges[from_city]:
        next_distance = distance + cost

        if next_distance < costs[to_city]:
            costs[to_city] = next_distance
            heapq.heappush(heap, (next_distance, to_city))
            prev_city[to_city] = from_city

print(costs[end])
paths = []

node = end

while True:
    paths.append(str(node + 1))
    node = prev_city[node]

    if node == start:
        break

paths.append(str(start + 1))
paths.reverse()

print(len(paths))
print(" ".join(paths))
