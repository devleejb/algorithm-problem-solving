from sys import stdin

input = stdin.readline

dp = [[[0, 0] for _ in range(31)] for _ in range(1_001)]

T, W = map(int, input().split())
drop_zones = [0] + [int(input()) - 1 for _ in range(T)]
res = 1

dp[1][0][0] = int(drop_zones[1] == 0)
dp[1][1][1] = int(drop_zones[1] == 1)

for i in range(2, T + 1):
    for j in range(0, W + 1):
        for k in range(2):
            plus_plum = int(drop_zones[i] == k)
            if j == 0:
                dp[i][j][k] = dp[i - 1][j][k] + plus_plum
            else:
                dp[i][j][k] = (
                    max(dp[i - 1][j][k], dp[i - 1][j - 1][int(not k)]) + plus_plum
                )
            res = max(res, dp[i][j][k])

print(res)
