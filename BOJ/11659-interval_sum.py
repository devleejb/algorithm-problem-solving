from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
sum_list = [0]
res_list = []

for i in range(N):
    sum_list.append(sum_list[i] + num_list[i])

for _ in range(M):
    i, j = map(int, input().split())
    res_list.append(sum_list[j] - sum_list[i - 1])

for res in res_list:
    print(res)
