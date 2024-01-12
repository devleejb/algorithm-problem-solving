num_list = list(map(int, input().split()))

asc = [i for i in range(1, 9)]
desc = [9 - i for i in range(1, 9)]

if num_list == asc:
    print("ascending")
elif num_list == desc:
    print("descending")
else:
    print("mixed")
