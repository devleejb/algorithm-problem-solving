N = int(input())
dp = [0] * 31

dp[0] = 1

for i in range(1, N + 1):
    if i - 2 >= 0:
        dp[i] += dp[i - 2] * 3

    j = 4

    while i - j >= 0:
        dp[i] += dp[i - j] * 2
        j += 2

print(dp[N])
