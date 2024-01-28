from sys import stdin, maxsize

input = stdin.readline

n = int(input())
m = int(input())
graph_list = [[maxsize for _ in range(n)] for _ in range(n)]


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

for i in range(n):
    for j in range(n):
        if graph_list[i][j] == maxsize:
            print(0, end=" ")
        else:
            print(graph_list[i][j], end=" ")
    print()
