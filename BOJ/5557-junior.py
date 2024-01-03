N = int(input())
num_list = [0] + list(map(int, input().split()))
prev_dp = [0] * 21

prev_dp[num_list[1]] = 1

for i in range(2, N):
    now_dp = [0] * 21
    for j in range(0, 21):
        if prev_dp[j]:
            subtracted = j - num_list[i]
            added = j + num_list[i]
            if subtracted >= 0:
                now_dp[subtracted] = now_dp[subtracted] + prev_dp[j]
            if added <= 20:
                now_dp[added] = now_dp[added] + prev_dp[j]
    prev_dp = now_dp

print(prev_dp[num_list[N]])
