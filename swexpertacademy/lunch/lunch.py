import sys
sys.stdin = open("sample_input.txt", "r")

import heapq
from collections import deque

T = int(input())

PERSON = 1
STAIR = 2


def comb_internal(people, idx, n, acc, res):
    if len(acc) == n:
        res.append(acc)
        return
    if len(people) == idx:
        return

    comb_internal(people, idx + 1, n, acc, res)
    new_acc = acc.copy()
    new_acc.append(people[idx])
    comb_internal(people, idx + 1, n, new_acc, res)



def comb(people, n):
    res = []

    comb_internal(people, 0, n, [], res)

    return res




for test_case in range(1, T + 1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    people = []
    stairs = []

    for row in range(N):
        for col in range(N):
            if maps[row][col] == PERSON:
                people.append((row, col))
            elif maps[row][col] >= STAIR:
                stairs.append((row, col, maps[row][col]))

    min_cost = 1_234_567_890
    people_set = set(people)

    for i in range(0, N + 1):
        combs = comb(people, i)

        for first_stair_people in combs:
            first_stair_people_set = set(first_stair_people)
            second_stair_people_set = people_set - first_stair_people_set
            first_stair_hq = []
            second_stair_hq = []

            first_stair_row, first_stair_col, first_cost = stairs[0]
            second_stair_row, second_stair_col, second_cost = stairs[1]

            for person_row, person_col in list(first_stair_people_set):
                dis = abs(first_stair_row - person_row) + abs(first_stair_col - person_col)
                heapq.heappush(first_stair_hq, dis)

            for person_row, person_col in list(second_stair_people_set):
                dis = abs(second_stair_row - person_row) + abs(second_stair_col - person_col)
                heapq.heappush(second_stair_hq, dis)

            max_time = 0
            first_q = deque([])
            while first_stair_hq:
                dis = heapq.heappop(first_stair_hq)

                while first_q and first_q[0] <= dis:
                    first_q.popleft()

                if len(first_q) < 3:
                    first_q.append(dis + first_cost)
                else:
                    dis = first_q[0]
                    heapq.heappush(first_stair_hq, dis)
            if first_q:
                max_time = max(max_time, max(first_q))

            second_q = deque([])
            while second_stair_hq:
                dis = heapq.heappop(second_stair_hq)

                while second_q and second_q[0] <= dis:
                    second_q.popleft()

                if len(second_q) < 3:
                    second_q.append(dis + second_cost)
                else:
                    dis = second_q[0]
                    heapq.heappush(second_stair_hq, dis)
            if second_q:
                max_time = max(max_time, max(second_q))


            min_cost = min(min_cost, max_time)

    print("#" + str(test_case), min_cost + 1)
