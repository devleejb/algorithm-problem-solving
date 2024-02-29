from sys import stdin, maxsize

input = stdin.readline

N, M, T = map(int, input().split())
graph = [[maxsize] * (N + 1) for _ in range(N + 1)]
cases = []

for i in range(N + 1):
    graph[i][i] = 0

for _ in range(M):
    u, v, h = map(int, input().split())
    graph[u][v] = min(graph[u][v], h)

for _ in range(T):
    cases.append(list(map(int, input().split())))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if j == k:
                continue
            graph[j][k] = min(graph[j][k], max(graph[j][i], graph[i][k]))

for start, end in cases:
    if graph[start][end] >= maxsize:
        print(-1)
    else:
        print(graph[start][end])
