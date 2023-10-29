from sys import stdin

input = stdin.readline
H, W = map(int, input().split())
h_list = list(map(int, input().split()))

rain_space = 0

for i in range(H):
    now_height = H - i

    wall_idx_list = []
    for j in range(W):
        if h_list[j] >= now_height:
            wall_idx_list.append(j)

    for j in range(1, len(wall_idx_list)):
        rain_space += wall_idx_list[j] - wall_idx_list[j - 1] - 1

print(rain_space)
