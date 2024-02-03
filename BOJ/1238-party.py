from sys import stdin, maxsize
import heapq

input = stdin.readline

N, M, X = map(int, input().split())
edges = [[maxsize] * N for _ in range(N)]
reverse_edges = [[maxsize] * N for _ in range(N)]
costs = [[maxsize] * N for _ in range(2)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    start -= 1
    end -= 1

    edges[start][end] = cost
    reverse_edges[end][start] = cost

for i in range(N):
    edges[i][i] = 0
    reverse_edges[i][i] = 0

def dijkstra(edges, type):
    heap = []
    visited = [False] * N
    costs[type][X - 1] = 0
    heapq.heappush(heap, (0, X - 1))

    while heap:
        cost, village = heapq.heappop(heap)

        if visited[village]:
            continue

        for to_village, cost in enumerate(edges[village]):
            next_cost = costs[type][village] + cost
            if costs[type][to_village] > next_cost:
                costs[type][to_village] = next_cost
                heapq.heappush(heap, (next_cost, to_village))

dijkstra(edges, 0)
dijkstra(reverse_edges, 1)

max_val = 0

for i in range(N):
    max_val = max(max_val, costs[0][i] + costs[1][i])

print(max_val)