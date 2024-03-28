from sys import stdin

input = stdin.readline

MAP_SIZE = 201
RIGHT = 0
UP = 1
LEFT = 2
BOTTOM = 3
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
N = int(input())
curves = [list(map(int, input().split())) for _ in range(N)]
maps = [[0] * MAP_SIZE for _ in range(MAP_SIZE)]

for col, row, d, g in curves:
    start = (row, col)
    end = (row + dr[d], col + dc[d])
    cur_gen = 0
    graph = [start, end]

    while cur_gen < g:
        cur_point = graph[-1]

        for point in reversed(graph[:-1]):
            row, col = point
            cur_row, cur_col = cur_point
            row_diff = cur_row - row
            col_diff = cur_col - col
            graph.append((graph[-1][0] - col_diff, graph[-1][1] + row_diff))

            cur_point = point
        cur_gen += 1

    for row, col in graph:
        maps[row * 2][col * 2] = 1

res = 0

dr = [-1, 1, 1, -1]
dc = [1, 1, -1, -1]

for row in range(1, MAP_SIZE, 2):
    for col in range(1, MAP_SIZE, 2):
        cnt = 0
        for i in range(4):
            next_row = row + dr[i]
            next_col = col + dc[i]
            if not (0 <= next_row < MAP_SIZE and 0 <= next_col < MAP_SIZE):
                break
            if maps[next_row][next_col] == 1:
                cnt += 1
        if cnt == 4:
            res += 1
print(res)
