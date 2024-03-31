from sys import stdin, setrecursionlimit, maxsize

setrecursionlimit(10**5)

input = stdin.readline

dr = [0, 1, 0]
dc = [1, 0, -1]

RIHGT, LEFT = 0, 1
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
dp = [[[-maxsize, -maxsize] for _ in range(M)] for _ in range(N)]

dp[0][0][RIHGT] = maps[0][0]
for i in range(1, M):
    dp[0][i][RIHGT] = dp[0][i - 1][RIHGT] + maps[0][i]

for i in range(1, N):
    for j in range(M):
        local_max = -maxsize

        if j > 0:
            local_max = dp[i][j - 1][RIHGT]

        local_max = max(local_max, max(dp[i - 1][j]))

        dp[i][j][RIHGT] = local_max + maps[i][j]
    for j in reversed(range(M)):
        local_max = -maxsize

        if j < M - 1:
            local_max = dp[i][j + 1][LEFT]

        local_max = max(local_max, max(dp[i - 1][j]))

        dp[i][j][LEFT] = local_max + maps[i][j]

print(max(dp[N - 1][M - 1]))
