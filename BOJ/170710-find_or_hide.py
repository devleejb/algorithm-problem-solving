from sys import stdin
from collections import deque

input = stdin.readline

MAX_IDX = 500_000
MIN_IDX = 0
N, K = map(int, input().split())
visited = [[False, False] for _ in range(500_001)]
q = deque([])
visited[N][0] = True

q.append((N, 0))

current_cost = 0
res = -1
t = 0

while q:
    K += t

    if K > MAX_IDX:
        break

    for _ in range(len(q)):
        position, cost = q.popleft()
        next_cost = cost + 1

        if position + 1 <= MAX_IDX and not visited[position + 1][next_cost % 2]:
            q.append((position + 1, next_cost))
            visited[position + 1][next_cost % 2] = True
        if position - 1 >= MIN_IDX and not visited[position - 1][next_cost % 2]:
            q.append((position - 1, next_cost))
            visited[position - 1][next_cost % 2] = True
        if position * 2 <= MAX_IDX and not visited[position * 2][next_cost % 2]:
            q.append((position * 2, next_cost))
            visited[position * 2][next_cost % 2] = True

    if visited[K][t % 2]:
        res = t
        break

    t += 1

print(res)
