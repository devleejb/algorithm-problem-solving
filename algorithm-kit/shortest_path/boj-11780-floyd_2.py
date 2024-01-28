# https://www.acmicpc.net/problem/11780
from sys import stdin, maxsize

input = stdin.readline

n = int(input())
m = int(input())
graph_list = [[maxsize for _ in range(n)] for _ in range(n)]
prev_list = [[i for _ in range(n)] for i in range(n)]


def track_route(from_city, to_city):
    if prev_list[from_city][to_city] != from_city:
        routes_left = track_route(from_city, prev_list[from_city][to_city])
        routes_right = track_route(prev_list[from_city][to_city], to_city)
        return routes_left + routes_right
    else:
        return [from_city + 1]


for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph_list[a][b] = min(graph_list[a][b], c)

for i in range(n):
    graph_list[i][i] = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph_list[j][k] > graph_list[j][i] + graph_list[i][k]:
                graph_list[j][k] = graph_list[j][i] + graph_list[i][k]
                prev_list[j][k] = i

for i in range(n):
    for j in range(n):
        if graph_list[i][j] == maxsize:
            print(0, end=" ")
        else:
            print(graph_list[i][j], end=" ")
    print()

for i in range(n):
    for j in range(n):
        if graph_list[i][j] == maxsize or graph_list[i][j] == 0:
            print(0)
            continue

        city = j
        path_list = track_route(i, j) + [j + 1]

        print(len(path_list), *path_list)
