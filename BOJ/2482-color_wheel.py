from sys import stdin

input = stdin.readline

DIVIDER = 1_000_000_003
NOT_INCLUDE_END = 0
INCLUE_END = 1

N = int(input())
K = int(input())
dp = [[[0, 0] for _ in range(1_001)] for _ in range(1_001)]

for i in reversed(range(1, N + 1)):
    if i == N:
        dp[1][i][INCLUE_END] = 1
    else:
        dp[1][i][NOT_INCLUDE_END] = 1 + dp[1][i + 1][NOT_INCLUDE_END]
        dp[1][i][INCLUE_END] = dp[1][i + 1][INCLUE_END]

for i in range(2, K + 1):
    for j in reversed(range(1, N)):
        local_sum_not_end = dp[i][j + 1][NOT_INCLUDE_END]
        local_sum_end = dp[i][j + 1][INCLUE_END]

        if j + 2 <= N:
            local_sum_not_end += dp[i - 1][j + 2][NOT_INCLUDE_END] % DIVIDER
            if j != 1:
                local_sum_end += dp[i - 1][j + 2][INCLUE_END] % DIVIDER

        dp[i][j][NOT_INCLUDE_END] = local_sum_not_end % DIVIDER
        dp[i][j][INCLUE_END] = local_sum_end % DIVIDER

print(sum(dp[K][1]) % DIVIDER)
