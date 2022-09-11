N = int(input())
board = [list(input()) for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
result = 0

for i in range(N):
    for j in range(N):
        for k in range(len(dr)):
            nr = i + dr[k]
            nc = j + dc[k]

            if ((nr - 1 == i and nc == j) or (nc - 1 == j and nr == i)):
                continue

            if (nr >= 0 and nc >= 0 and nr < N and nc < N and board[i][j] != board[nr][nc]):
                board[i][j], board[nr][nc] = board[nr][nc], board[i][j]
                maxRow, maxCol = 0, 0

                for row in range(N):
                    nowRowCount = 1

                    for col in range(1, N):
                        if (board[row][col - 1] == board[row][col]):
                            nowRowCount += 1

                            maxRow = max(maxRow, nowRowCount)
                        else:
                            nowRowCount = 1

                        result = max(result, maxRow)

                for col in range(N):
                    nowColCount = 1

                    for row in range(1, N):
                        if (board[row - 1][col] == board[row][col]):
                            nowColCount += 1

                            maxCol = max(maxCol, nowColCount)
                        else:
                            nowColCount = 1

                        result = max(result, maxCol)

                board[i][j], board[nr][nc] = board[nr][nc], board[i][j]


print(result)
