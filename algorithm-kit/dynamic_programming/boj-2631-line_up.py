# https://www.acmicpc.net/problem/2631
N = int(input())
num_list = [int(input()) for _ in range(N)]
dp = [1] * 200
res = 0

for i, num in enumerate(num_list):
    for j in range(0, i):
        if num_list[j] < num:
            dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])

print(len(num_list) - res)
