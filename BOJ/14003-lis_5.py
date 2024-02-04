from sys import stdin
from bisect import bisect_left
from collections import deque

input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
lis = []
record = [0] * N

lis.append(A[0])
record[0] = 1

for i in range(1, N):
    a = bisect_left(lis, A[i])

    if a == len(lis):
        lis.append(A[i])
        record[i] = len(lis)
    else:
        lis[a] = A[i]
        record[i] = a + 1

print(len(lis))

target = len(lis)
i = N - 1
res_list = deque([])

while i >= 0:
    if record[i] == target:
        target -= 1
        res_list.appendleft(A[i])
    i -= 1

print(*res_list)