from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
costs = [0] * N
indegrees = [0] * N
res = [0] * N
max_costs = [0] * N
edges = [[] for _ in range(N)]

for i in range(N):
    items = list(map(int, input().split()))
    costs[i] = items[0]

    for prior in range(1, len(items) - 1):
        edges[items[prior] - 1].append(i)
        indegrees[i] += 1

q = deque([])

for i, indegree in enumerate(indegrees):
    if indegree == 0:
        q.append((i, 0))


while q:
    idx, cost = q.popleft()
    cost += costs[idx]
    res[idx] = cost

    for edge in edges[idx]:
        indegrees[edge] -= 1
        max_costs[edge] = max(max_costs[edge], cost)

        if indegrees[edge] == 0:
            q.append((edge, max_costs[edge]))


for r in res:
    print(r)
