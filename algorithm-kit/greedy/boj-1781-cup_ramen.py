# https://www.acmicpc.net/problem/1781
# 1. 핵심 아이디어 추론
#    데드라인을 오름차순으로 정렬하고, 같은 데드라인이라면 컵라면을 더 많이 주는 순으로 정렬한다.
#    현재 Deadline에서 가장 많은 컵라면을 주는 문제를 선택하고, 이전의 선택한 문제 중 컵라면을 더 적게 주는 문제가 있다면 제외하고 현재 문제를 선택한다.
# 2. 정당성 분석
#    해당 데드라인 내에서 더 많은 컵라면을 받을 수 없다.

from sys import stdin
import heapq

input = stdin.readline
N = int(input())
problem_list = [list(map(int, input().split())) for _ in range(N)]
problem_list.sort(key=lambda x: (x[0], -x[1]))
heap = []

time = 0

for problem in problem_list:
    deadline, cup = problem
    if deadline <= time:
        if heap[0] < cup:
            heapq.heappop(heap)
            heapq.heappush(heap, cup)
    else:
        time += 1
        heapq.heappush(heap, problem[1])


print(sum(heap))
