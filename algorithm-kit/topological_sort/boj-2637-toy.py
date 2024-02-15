# https://www.acmicpc.net/problem/2637

from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
M = int(input())
edges = [[] for _ in range(N + 1)]
indegrees = [0] * (N + 1)
costs = [{} for _ in range(N + 1)] 
default_component = {}

for _ in range(M):
    X, Y, K = map(int, input().split())
    edges[Y].append((X, K))
    indegrees[X] += 1

q = deque([])

for i, indegree in enumerate(indegrees):
    if i == 0:
        continue

    if indegree == 0:
        q.append(i)
        default_component[i] = True
        costs[i] = { i: 1 }

while q:
    popped = q.popleft()

    for to, cnt in edges[popped]:
        indegrees[to] -= 1

        for key in costs[popped]:
            if key in costs[to].keys():
                costs[to][key] += costs[popped][key] * cnt
            else:
                costs[to][key] = costs[popped][key] * cnt

        if indegrees[to] == 0:
            q.append(to)

keys = costs[N].keys()

for key in sorted(keys):
    print(key, costs[N][key])