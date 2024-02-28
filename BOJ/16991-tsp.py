from sys import stdin, maxsize
import math

input = stdin.readline


N = int(input())
positions = [list(map(int, input().split())) for _ in range(N)]
edges = [[] for _ in range(N)]
ALL_VISITED = 2**N - 1
res = maxsize
global_visited = [[maxsize] * ALL_VISITED for _ in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        distance = math.sqrt(
            (positions[i][0] - positions[j][0]) ** 2
            + (positions[i][1] - positions[j][1]) ** 2
        )
        edges[i].append((j, distance))
        edges[j].append((i, distance))


def dfs(city, visited, cost):
    global res
    if visited == ALL_VISITED:
        res = min(res, cost + edges[city][0][1])
        return

    if global_visited[city][visited] <= cost:
        return

    global_visited[city][visited] = cost

    for to_city, edge_cost in edges[city]:
        if visited & (1 << to_city) != 0:
            continue
        next_visited = visited | (1 << to_city)
        dfs(to_city, next_visited, cost + edge_cost)


dfs(0, 1, 0)

print(res)
