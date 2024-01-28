RED = 0
GREEN = 1
BLUE = 2

N = int(input())
cost_list = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]
dp[0] = cost_list[0]

for i in range(1, N):
    dp[i][RED] = min(dp[i - 1][GREEN], dp[i - 1][BLUE]) + cost_list[i][RED]
    dp[i][GREEN] = min(dp[i - 1][RED], dp[i - 1][BLUE]) + cost_list[i][GREEN]
    dp[i][BLUE] = min(dp[i - 1][RED], dp[i - 1][GREEN]) + cost_list[i][BLUE]

print(min(dp[N - 1]))
