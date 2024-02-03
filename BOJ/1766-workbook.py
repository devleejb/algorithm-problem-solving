from sys import stdin
import heapq

input = stdin.readline

N, M = map(int, input().split())
edges = [[] for _ in range(N)]
ingoings = [0] * N

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    edges[A].append(B)
    ingoings[B] += 1

heap = []
for i in range(N):
    if ingoings[i] == 0:
        heapq.heappush(heap, i)

res = []

while heap:
    workbook = heapq.heappop(heap)
    res.append(workbook + 1)

    for i in edges[workbook]:
        if ingoings[i] > 0:
            ingoings[i] -= 1

            if ingoings[i] == 0:
                heapq.heappush(heap, i)

print(*res)