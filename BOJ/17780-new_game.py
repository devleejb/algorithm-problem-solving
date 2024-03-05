from sys import stdin

input = stdin.readline

WHITE = 0
RED = 1
BLUE = 2

RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
reverse_dir = [1, 0, 3, 2]

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
current_board = [[[] for _ in range(N)] for _ in range(N)]
positions = [[0, 0] for _ in range(K)]
dirs = [0] * K

for i in range(K):
    row, col, dir = map(int, input().split())
    row -= 1
    col -= 1
    dir -= 1
    positions[i] = [row, col]
    dirs[i] = dir
    current_board[row][col].append(i)

turn = 0
res = -1

while True:
    finished = False
    i = 0
    while i < K:
        row, col = positions[i]
        bottom = current_board[row][col][0]
        bottom_dir = dirs[bottom]
        nr = row + dr[bottom_dir]
        nc = col + dc[bottom_dir]

        if bottom != i:
            i += 1
            continue

        if 0 <= nr < N and 0 <= nc < N:
            if board[nr][nc] == WHITE:
                for horse in current_board[row][col]:
                    current_board[nr][nc].append(horse)
                    positions[horse] = [nr, nc]
                current_board[row][col] = []
                if len(current_board[nr][nc]) >= 4:
                    finished = True
                    break
            elif board[nr][nc] == RED:
                for horse in reversed(current_board[row][col]):
                    current_board[nr][nc].append(horse)
                    positions[horse] = [nr, nc]
                current_board[row][col] = []
                if len(current_board[nr][nc]) >= 4:
                    finished = True
                    break
            else:
                bottom_dir = dirs[bottom] = reverse_dir[dirs[bottom]]
                nr = row + dr[bottom_dir]
                nc = col + dc[bottom_dir]
                if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] != BLUE:
                    continue
        else:
            bottom_dir = dirs[bottom] = reverse_dir[dirs[bottom]]
            nr = row + dr[bottom_dir]
            nc = col + dc[bottom_dir]
            if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] != BLUE:
                continue
        i += 1
    turn += 1
    if turn > 1000 or finished:
        res = turn
        break

print(-1 if turn > 1000 else turn)
