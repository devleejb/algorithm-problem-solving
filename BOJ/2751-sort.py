N = int(input())
table = [0] * 2_000_001
num_list = [int(input()) for _ in range(N)]

for num in num_list:
    table[num + 1_000_000] += 1

for i, cnt in enumerate(table):
    if cnt:
        print(i - 1_000_000)
