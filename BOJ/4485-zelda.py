from sys import stdin, maxsize
from collections import deque

input = stdin.readline
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def sol(N, board):
    res = maxsize
    visited = [[maxsize] * N for _ in range(N)]
    q = deque([(0, 0, board[0][0])])

    while q:
        row, col, cost = q.popleft()

        if row == N - 1 and col == N - 1:
            res = min(res, cost)
            continue

        if visited[row][col] < cost:
            continue

        for i in range(4):
            next_row = row + dr[i]
            next_col = col + dc[i]

            if 0 <= next_row < N and 0 <= next_col < N:
                next_cost = cost + board[next_row][next_col]
                if visited[next_row][next_col] > next_cost:
                    visited[next_row][next_col] = next_cost
                    q.append((next_row, next_col, next_cost))

    return res


res_list = []

while True:
    N = int(input())

    if N == 0:
        break

    board = [list(map(int, input().rstrip().split())) for _ in range(N)]
    res_list.append(sol(N, board))

for i in range(len(res_list)):
    print(f"Problem {i + 1}: {res_list[i]}")
