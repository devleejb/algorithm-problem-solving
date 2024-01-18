# https://www.acmicpc.net/problem/2036

N = int(input())
plus_list = []
minus_list = []
res = 0
zero_cnt = 0

for _ in range(N):
    n = int(input())

    if n == 1:
        res += 1
    elif n == 0:
        zero_cnt += 1
    elif n > 0:
        plus_list.append(n)
    else:
        minus_list.append(n)

minus_list.sort(reverse=True)
plus_list.sort()

if len(minus_list) % 2 != 0:
    if zero_cnt == 0:
        res += minus_list[0]
    minus_list = minus_list[1:]

for i in range(0, len(minus_list), 2):
    res += minus_list[i] * minus_list[i + 1]

if len(plus_list) % 2 != 0:
    res += plus_list[0]
    plus_list = plus_list[1:]

for i in range(0, len(plus_list), 2):
    res += plus_list[i] * plus_list[i + 1]

print(res)
