# https://www.acmicpc.net/problem/2623
from sys import stdin
from collections import deque

input = stdin.readline

N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]
degrees = [0] * (N + 1)

for _ in range(M):
    orders = list(map(int, input().split()))
    orders = orders[1:]

    for i in range(len(orders) - 1):
        start = orders[i]
        end = orders[i + 1]
        edges[start].append(end)
        degrees[end] += 1

q = deque([])

for i, degree in enumerate(degrees):
    if i == 0 or degree != 0:
        continue
    q.append(i)

res_list = []

while q:
    popped = q.popleft()
    res_list.append(popped)
    for end in edges[popped]:
        degrees[end] -= 1
        if degrees[end] == 0:
            q.append(end)

if len(res_list) != N:
    print(0)
else:
    for res in res_list:
        print(res)
