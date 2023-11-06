from sys import stdin

input = stdin.readline

N, S = map(int, input().split())
num_list = list(map(int, input().split()))

INIT = 123456789
sum = 0
j = 0
min_len = INIT

for i in range(N):
    while sum < S and j < N:
        sum += num_list[j]
        j += 1

    if sum >= S:
        min_len = min(min_len, j - i)

    sum -= num_list[i]

if min_len == INIT:
    print(0)
else:
    print(min_len)
