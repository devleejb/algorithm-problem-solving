from sys import stdin
import heapq

input = stdin.readline

N = int(input())

max_heap = []
min_heap = []

res_list = []

for i in range(1, N + 1):
    num = int(input())
    if i == 1:
        heapq.heappush(max_heap, -num)
    else:
        max_heap_top = -max_heap[0]
        if len(max_heap) > len(min_heap):
            if max_heap_top > num:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
                heapq.heappush(max_heap, -num)
            else:
                heapq.heappush(min_heap, num)
        else:
            if max_heap_top > num:
                heapq.heappush(max_heap, -num)
            else:
                heapq.heappush(min_heap, num)
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

    res_list.append(-max_heap[0])

for res in res_list:
    print(res)
