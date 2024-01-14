from sys import stdin

input = stdin.readline

N = int(input())
num_list = []
dp = [[0 for _ in range(4)] for _ in range(N)]

for _ in range(N):
    num_list.append(int(input()))

dp[0][1] = num_list[0]
if len(num_list) > 1:
    dp[1][1] = num_list[1]

for i, num in enumerate(num_list[1:]):
    i = i + 1
    if i - 2 >= 0:
        dp[i][1] = max(dp[i - 2]) + num
    dp[i][2] = dp[i - 1][1] + num

print(max(dp[N - 1]))
