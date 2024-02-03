# https://www.acmicpc.net/problem/17182

from sys import stdin, maxsize

input = stdin.readline

N, K = map(int, input().split())
costs = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])

def visit(planet, cost, visited):
    visited = visited | (1 << planet)

    if visited == 2 ** N - 1:
        return cost

    min_cost = maxsize

    for i, edge in enumerate(costs[planet]):
        if visited & (1 << i) == 0:
            min_cost = min(min_cost, visit(i, cost + edge, visited))

    return min_cost

print(visit(K, 0, 0))