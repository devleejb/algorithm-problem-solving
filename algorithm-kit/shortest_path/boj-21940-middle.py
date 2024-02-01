# https://www.acmicpc.net/problem/21940
from sys import stdin, maxsize

input = stdin.readline

N, M = map(int, input().split())
edges = [[maxsize] * N for _ in range(N)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    start -= 1
    end -= 1
    edges[start][end] = cost

for i in range(N):
    edges[i][i] = 0

K = int(input())
homes = list(map(int, input().split()))

for i in range(N):
    for j in range(N):
        for k in range(N):
            edges[j][k] = min(edges[j][k], edges[j][i] + edges[i][k])

res = maxsize
mids = []

for i in range(N):
    max_val = 0
    for home in homes:
        home -= 1
        max_val = max(max_val, edges[home][i] + edges[i][home])

    if max_val >= maxsize:
        continue

    if res > max_val:
        res = max_val
        mids = [i + 1]
    elif res == max_val:
        mids.append(i + 1)

print(*mids)
