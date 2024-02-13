# https://www.acmicpc.net/problem/2056
from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
edges = [[] for _ in range(N + 1)]
costs = [0]
cost_sum = [0] * (N + 1)
indegrees = [0] * (N + 1)

for i in range(1, N + 1):
    inputs = list(map(int, input().split()))
    costs.append(inputs[0])
    tmp_edges = inputs[2:]

    for edge in tmp_edges:
        edges[edge].append(i)
        indegrees[i] += 1

q = deque([])

for i, indegree in enumerate(indegrees):
    if i == 0:
        continue

    if indegree == 0:
        q.append(i)
        cost_sum[i] = costs[i]

while q:
    popped = q.popleft()

    for edge in edges[popped]:
        indegrees[edge] -= 1
        cost_sum[edge] = max(cost_sum[edge], cost_sum[popped] + costs[edge])

        if indegrees[edge] == 0:
            q.appendleft(edge)

print(max(cost_sum))