# https://www.acmicpc.net/problem/1309
N = int(input())
dp = [[0, 0, 0] for _ in range(100_000)]
dp[0] = [1, 1, 1]
DIVIDER = 9_901

for i in range(1, N):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % DIVIDER
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % DIVIDER
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % DIVIDER

print(sum(dp[N - 1]) % DIVIDER)
