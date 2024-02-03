from sys import stdin
from collections import deque

input = stdin.readline

T = int(input())
results = []

for _ in range(T):
    N, K = map(int, input().split())
    visited = [False] * N
    times = list(map(int, input().split()))
    edges = [[] for _ in range(N)]
    ingoings = [0] * N
    costs = [0] * N
    q = deque([])

    for _ in range(K):
        X, Y = map(int, input().split())
        X -= 1
        Y -= 1
        edges[X].append(Y)
        ingoings[Y] += 1

    W = int(input())

    for i in range(N):
        if ingoings[i] == 0:
            q.append(i)
            costs[i] = times[i]

    while q:
        city = q.popleft()

        for to_city in edges[city]:
            if ingoings[to_city] > 0:
                ingoings[to_city] -= 1
            else:
                continue

            if ingoings[to_city] == 0:
                q.append(to_city) 
            
            costs[to_city] = max(costs[to_city], costs[city] + times[to_city])

    results.append(costs[W - 1])

for result in results:
    print(result)