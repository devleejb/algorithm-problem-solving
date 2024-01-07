# https://www.acmicpc.net/problem/18185
# 1. 핵심 아이디어 추론
#    i + 1번째가 i + 2번째보다 수요가 많은 경우, 2묶음 -> 3묶음 -> 1묶음 순서로 구매한다.
#    i + 2번째가 i + 1번째보다 수요가 많은 경우, 3묶음 -> 2묶음 -> 1묶음 순서로 구매한다.
# 2. 정당성 분석
#    최대한 2묶음, 3묶음으로 많이 구매를 하는 것이 더 저렴하다.

from sys import stdin

input = stdin.readline

N = int(input())
demand_list = list(map(int, input().split())) + [0]

i = 0
cost = 0

while i < N:
    if i + 2 < N and demand_list[i + 1] > demand_list[i + 2]:
        spend_cnt = min(demand_list[i], demand_list[i + 1] - demand_list[i + 2])
        demand_list[i] -= spend_cnt
        demand_list[i + 1] -= spend_cnt
        cost += 5 * spend_cnt

        spend_cnt = min(demand_list[i], demand_list[i + 1], demand_list[i + 2])
        demand_list[i] -= spend_cnt
        demand_list[i + 1] -= spend_cnt
        demand_list[i + 2] -= spend_cnt
        cost += 7 * spend_cnt
    elif i + 1 < N:
        spend_cnt = min(demand_list[i], demand_list[i + 1], demand_list[i + 2])
        demand_list[i] -= spend_cnt
        demand_list[i + 1] -= spend_cnt
        demand_list[i + 2] -= spend_cnt
        cost += 7 * spend_cnt

        spend_cnt = min(demand_list[i], demand_list[i + 1])
        demand_list[i] -= spend_cnt
        demand_list[i + 1] -= spend_cnt
        cost += 5 * spend_cnt

    cost += 3 * demand_list[i]
    demand_list[i] = 0

    i = i + 1


print(cost)
