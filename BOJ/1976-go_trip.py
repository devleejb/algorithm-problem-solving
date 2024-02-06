from sys import stdin, maxsize

input = stdin.readline

N = int(input())
M = int(input())
edges = [list(map(int, input().split())) for _ in range(N)]
roadmap = list(map(int, input().split()))

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if edges[i][j] == 0:
            edges[i][j] = maxsize

for k in range(N):
    for i in range(N):
        for j in range(N):
            edges[i][j] = min(edges[i][j], edges[i][k] + edges[k][j])

is_available = True

for i in range(1, M):
    if edges[roadmap[i - 1] - 1][roadmap[i] - 1] >= maxsize:
        is_available = False
        break

print("YES" if is_available else "NO")