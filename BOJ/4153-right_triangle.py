side_list = list(map(int, input().split()))
res_list = []

while not 0 in side_list:
    side_list.sort()
    res_list.append(pow(side_list[2], 2) == pow(side_list[0], 2) + pow(side_list[1], 2))
    side_list = list(map(int, input().split()))

for res in res_list:
    if res:
        print("right")
    else:
        print("wrong")
