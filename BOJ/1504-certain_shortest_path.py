from sys import stdin, maxsize
from heapq import heappop, heappush

input = stdin.readline

N, E = map(int, input().split())
edges = {}


def get_shortest_cost(a, b):
    hq = [(0, a)]
    visited = [False] * (N + 1)
    costs = [-1] * (N + 1)

    while hq:
        cost, vertex = heappop(hq)
        visited[vertex] = True
        costs[vertex] = cost

        if vertex == b:
            break

        for to_vertex, weight in edges[vertex]:
            if visited[to_vertex]:
                continue
            next_cost = cost + weight
            heappush(hq, (next_cost, to_vertex))

    return costs[b]


for i in range(1, N + 1):
    edges[i] = []


for _ in range(E):
    a, b, c = map(int, input().split())

    edges[a].append((b, c))
    edges[b].append((a, c))

v1, v2 = map(int, input().split())

a_v1 = get_shortest_cost(1, v1)
v1_v2 = get_shortest_cost(v1, v2)
v2_c = get_shortest_cost(v2, N)

if a_v1 == -1 or v1_v2 == -1 or v2_c == -1:
    path1 = -1
else:
    path1 = a_v1 + v1_v2 + v2_c

a_v2 = get_shortest_cost(1, v2)
v2_v1 = get_shortest_cost(v2, v1)
v1_c = get_shortest_cost(v1, N)

if a_v2 == -1 or v2_v1 == -1 or v1_c == -1:
    path2 = -1
else:
    path2 = a_v2 + v2_v1 + v1_c

if path1 == -1 and path2 == -1:
    print(-1)
elif path1 == -1:
    print(path2)
elif path2 == -1:
    print(path1)
else:
    print(min(path1, path2))
