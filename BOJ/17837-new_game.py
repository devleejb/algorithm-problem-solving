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
    positions[i] = [row, col, 0]
    dirs[i] = dir
    current_board[row][col].append(i)

turn = 0
res = -1

while True:
    finished = False
    i = 0
    while i < K:
        row, col, floor = positions[i]
        floor_dir = dirs[i]
        nr = row + dr[floor_dir]
        nc = col + dc[floor_dir]

        if 0 <= nr < N and 0 <= nc < N:
            if board[nr][nc] == WHITE:
                for horse in current_board[row][col][floor:]:
                    positions[horse] = [nr, nc, len(current_board[nr][nc])]
                    current_board[nr][nc].append(horse)
                current_board[row][col] = current_board[row][col][:floor]
                if len(current_board[nr][nc]) >= 4:
                    finished = True
                    break
            elif board[nr][nc] == RED:
                for horse in reversed(current_board[row][col][floor:]):
                    positions[horse] = [nr, nc, len(current_board[nr][nc])]
                    current_board[nr][nc].append(horse)
                current_board[row][col] = current_board[row][col][:floor]
                if len(current_board[nr][nc]) >= 4:
                    finished = True
                    break
            else:
                i_dir = dirs[i] = reverse_dir[dirs[i]]
                nr = row + dr[i_dir]
                nc = col + dc[i_dir]
                if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] != BLUE:
                    continue
        else:
            i_dir = dirs[i] = reverse_dir[dirs[i]]
            nr = row + dr[i_dir]
            nc = col + dc[i_dir]
            if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] != BLUE:
                continue
        i += 1
    turn += 1

    if turn > 1000 or finished:
        res = turn
        break

print(-1 if turn > 1000 else turn)
