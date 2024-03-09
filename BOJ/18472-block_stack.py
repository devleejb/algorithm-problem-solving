from sys import stdin

input = stdin.readline

DIVIDER = 10_007
N, M, H = map(int, input().split())
dp = [[0] * (H + 1) for _ in range(N + 1)]
available_block_heights = [[]] + [list(map(int, input().split())) for _ in range(N)]
dp[0][0] = 1

for i in range(1, N + 1):
    for j, occurrence in enumerate(dp[i - 1]):
        if occurrence > 0:
            dp[i][j] += occurrence % DIVIDER
            dp[i][j] %= DIVIDER
            for height in available_block_heights[i]:
                if j + height <= H:
                    dp[i][j + height] += occurrence % DIVIDER
                    dp[i][j + height] %= DIVIDER


print(dp[N][H])
