N = int(input())
coordinate_list = []

for i in range(N):
    coordinate_list.append(tuple(map(int, input().split())))

coordinate_list.sort(key=lambda x: (x[0], x[1]))

for coordinate in coordinate_list:
    print(coordinate[0], coordinate[1])
