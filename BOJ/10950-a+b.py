T = int(input())
num_list = [list(map(int, input().split())) for _ in range(T)]
res_list = []

for a, b in num_list:
    res_list.append(a + b)

for res in res_list:
    print(res)
