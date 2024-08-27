from sys import stdin

input = stdin.readline

N = int(input().rstrip())
A = [int(input().rstrip()) for _ in range(N)]
A_E = list(enumerate(A))

A_E.sort(key=lambda k: (k[1], k[0]))

res = 0

for i in range(N):
    res = max(A_E[i][0] - i + 1, res)

print(res)
