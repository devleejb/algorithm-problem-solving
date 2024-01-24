# https://www.acmicpc.net/problem/1562

DIVIDER = 1_000_000_000
N = int(input())
dp = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(100)]

for i in range(1, 10):
    dp[0][i][1 << i] = 1

for i in range(N - 1):
    for j in range(10):
        for k in range(1024):
            if dp[i][j][k] == 0:
                continue
            if j + 1 <= 9:
                dp[i + 1][j + 1][k | 1 << (j + 1)] += dp[i][j][k] % DIVIDER
            if j - 1 >= 0:
                dp[i + 1][j - 1][k | 1 << (j - 1)] += dp[i][j][k] % DIVIDER

res = 0

for i in range(10):
    res += dp[N - 1][i][1023]
    res %= DIVIDER
print(res % DIVIDER)
