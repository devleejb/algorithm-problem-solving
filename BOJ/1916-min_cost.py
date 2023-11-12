from sys import stdin, maxsize

input = stdin.readline

N = int(input())
M = int(input())
edge_list = [list(map(int, input().split())) for _ in range(M)]
start, end = map(int, input().split())
cost_list = [maxsize for _ in range(N + 1)]
cost_list[start] = 0

for _ in range(N - 1):
    for edge in edge_list:
        edge_start, edge_end, edge_cost = edge

        if cost_list[edge_start] == maxsize:
            continue

        cost_list[edge_end] = min(
            cost_list[edge_end], cost_list[edge_start] + edge_cost
        )


print(cost_list[end])
