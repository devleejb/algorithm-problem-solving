# https://www.acmicpc.net/problem/14503
import sys

sys.setrecursionlimit(10**7)

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
EMPTY = 0
WALL = 1
CLEANED = 2

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
res = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(r, c, d):
    global res
    if room[r][c] == EMPTY:
        room[r][c] = CLEANED
        res += 1

    condition_2 = True
    for i in range(4):
        nr = r + dy[i]
        nc = c + dx[i]

        if 0 <= nr and nr < N and 0 <= nc and nc < M and room[nr][nc] == EMPTY:
            condition_2 = False

    if condition_2:
        delta = [0, 0]
        if d == NORTH:
            delta = [0, 1]
        elif d == EAST:
            delta = [-1, 0]
        elif d == SOUTH:
            delta = [0, -1]
        elif d == WEST:
            delta = [1, 0]
        nr = r + delta[1]
        nc = c + delta[0]

        if 0 <= nr and nr < N and 0 <= nc and nc < M and room[nr][nc] != WALL:
            return dfs(nr, nc, d)
        else:
            return

    delta = [0, 0]
    nd = NORTH
    if d == NORTH:
        nd = WEST
        delta = [-1, 0]
    elif d == EAST:
        nd = NORTH
        delta = [0, -1]
    elif d == SOUTH:
        nd = EAST
        delta = [1, 0]
    elif d == WEST:
        nd = SOUTH
        delta = [0, 1]
    nr = r + delta[1]
    nc = c + delta[0]
    if 0 <= nr and nr < N and 0 <= nc and nc < M and room[nr][nc] == EMPTY:
        return dfs(nr, nc, nd)
    else:
        return dfs(r, c, nd)


dfs(r, c, d)

print(res)
