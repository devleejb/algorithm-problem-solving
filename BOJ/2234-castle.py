from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]
disjoint_set = [i for i in range(N * M)]
disjoint_set_size = [1 for _ in range(N * M)]
dir = {1: [0, -1], 2: [-1, 0], 4: [0, 1], 8: [1, 0]}


def find_parent(a):
    if disjoint_set[a] != a:
        disjoint_set[a] = find_parent(disjoint_set[a])
    return disjoint_set[a]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a > b:
        disjoint_set[a] = b
        disjoint_set_size[b] += disjoint_set_size[a]
    elif a < b:
        disjoint_set[b] = a
        disjoint_set_size[a] += disjoint_set_size[b]


def dfs(row, col):
    visited[row][col] = True
    wall = 1
    cnt = 1

    while wall < 16:
        exists = castle[row][col] & wall
        if not exists:
            dr, dc = dir[wall]
            nr = row + dr
            nc = col + dc

            if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc]:
                cnt += dfs(nr, nc)
                union(row * N + col, nr * N + nc)

        wall = wall << 1

    return cnt


def if_merge_cnt(row, col):
    wall = 1
    max_cnt = 0

    while wall < 16:
        exists = castle[row][col] & wall
        if exists:
            dr, dc = dir[wall]
            nr = row + dr
            nc = col + dc

            if 0 <= nr < M and 0 <= nc < N:
                now_parent = find_parent(row * N + col)
                next_parent = find_parent(nr * N + nc)

                if now_parent != next_parent:
                    max_cnt = max(
                        max_cnt,
                        disjoint_set_size[now_parent] + disjoint_set_size[next_parent],
                    )

        wall = wall << 1

    return max_cnt


room_cnt = 0
max_room_size = 0

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            max_room_size = max(max_room_size, dfs(i, j))
            room_cnt += 1

max_if_merge_cnt = 0

for i in range(M):
    for j in range(N):
        max_if_merge_cnt = max(max_if_merge_cnt, if_merge_cnt(i, j))

print(room_cnt)
print(max_room_size)
print(max_if_merge_cnt)
