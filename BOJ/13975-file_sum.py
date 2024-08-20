from sys import stdin
import heapq

input = stdin.readline

T = int(input().strip())
res_list = []

for _ in range(T):
    K = int(input())
    hq = []

    for num in list(map(int, input().split())):
        heapq.heappush(hq, num)

    sum = 0

    while len(hq) >= 2:
        num1 = heapq.heappop(hq)
        num2 = heapq.heappop(hq)

        sum += num1 + num2
        heapq.heappush(hq, num1 + num2)

    res_list.append(sum)

for res in res_list:
    print(res)
