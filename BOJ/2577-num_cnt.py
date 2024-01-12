res = 1
num_cnt_list = [0 for _ in range(10)]

for i in range(3):
    res *= int(input())

for c in str(res):
    num_cnt_list[int(c)] += 1

for i in range(10):
    print(num_cnt_list[i])
