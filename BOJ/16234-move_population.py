from sys import stdin, setrecursionlimit

setrecursionlimit(10**5)
input = stdin.readline

N, L, R = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def dfs(r, c, visited, union):
    visited[r][c] = True
    union_cnt = maps[r][c]
    union.append((r, c))

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if not (0 <= nr < N and 0 <= nc < N):
            continue

        if not visited[nr][nc] and L <= abs(maps[nr][nc] - maps[r][c]) <= R:
            _, local_union_cnt = dfs(nr, nc, visited, union)
            union_cnt += local_union_cnt

    return (union, union_cnt)


res = 0

while True:
    is_active_turn = False
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union, union_cnt = dfs(i, j, visited, [])
                if len(union) > 1:
                    average = union_cnt // len(union)
                    for r, c in union:
                        maps[r][c] = average
                    is_active_turn = True

    if is_active_turn:
        res += 1
    else:
        break

print(res)
