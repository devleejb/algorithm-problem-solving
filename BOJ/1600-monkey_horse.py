from collections import deque

K = int(input())
W, H = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(H)]
visited = [[{} for _ in range(W)] for _ in range(H)]


horse_dr = [-2, -1, 1, 2, 2, 1, -1, -2]
horse_dc = [1, 2, 2, 1, -1, -2, -2, -1]
monkey_dr = [-1, 0, 1, 0]
monkey_dc = [0, 1, 0, -1]
OBSTACLE = 1


def visit(point, dr, dc):
    cur_row, cur_col = point
    visited_points = []

    for i in range(len(dr)):
        next_row = cur_row + dr[i]
        next_col = cur_col + dc[i]

        if not (0 <= next_row < H and 0 <= next_col < W):
            continue

        if maps[next_row][next_col] == OBSTACLE:
            continue

        visited_points.append((next_row, next_col))

    return visited_points


def dfs():
    q = deque([])

    # (point, cur_K, cur_cost)
    q.append(((0, 0), K, 0))

    while q:
        cur_point, cur_K, cur_cost = q.popleft()
        cur_row, cur_col = cur_point
        visited_points = []
        next_cost = cur_cost + 1

        if cur_K in visited[cur_row][cur_col]:
            continue

        visited[cur_row][cur_col][cur_K] = True

        if cur_row == H - 1 and cur_col == W - 1:
            return cur_cost

        if cur_K > 0:
            horse_visited_points = visit(cur_point, horse_dr, horse_dc)
            visited_points += [(point, cur_K - 1) for point in horse_visited_points]

        monkey_visited_points = visit(cur_point, monkey_dr, monkey_dc)
        visited_points += [(point, cur_K) for point in monkey_visited_points]

        for point, next_K in visited_points:
            next_row, next_col = point

            if next_K in visited[next_row][next_col]:
                continue

            q.append((point, next_K, next_cost))

    return -1


print(dfs())
