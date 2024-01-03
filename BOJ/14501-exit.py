from sys import stdin

input = stdin.readline


N = int(input())
T = []
P = []
dp = [0 for _ in range(N + 1)]
prev_max = 0

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for start in range(N):
    target = T[start] + start
    prev_max = max(prev_max, dp[start])

    if target > N:
        continue

    new_val = prev_max + P[start]
    dp[target] = max(new_val, dp[target])

print(max(dp))
