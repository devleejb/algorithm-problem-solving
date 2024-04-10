from sys import stdin, maxsize
from copy import deepcopy
from math import sqrt

input = stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
homes = []
chickens = []

EMPTY = 0
HOME = 1
CHICKEN = 2

for row in range(N):
    for col in range(N):
        if maps[row][col] == HOME:
            homes.append((row, col))
        elif maps[row][col] == CHICKEN:
            chickens.append((row, col))


def calc_chicken_len(selected_chickens):
    min_lens = [maxsize] * len(homes)

    for chicken_idx in selected_chickens:
        row, col = chickens[chicken_idx]

        for i, home in enumerate(homes):
            home_row, home_col = home
            dis = abs(row - home_row) + abs(col - home_col)
            min_lens[i] = min(min_lens[i], dis)

    return sum(min_lens)


res = maxsize


def select_chicken(idx, selected_chickens):
    global res
    if len(selected_chickens) == M:
        tmp_res = calc_chicken_len(selected_chickens)
        res = min(res, tmp_res)

    if idx == len(chickens):
        return

    select_chicken(idx + 1, deepcopy(selected_chickens))
    new_chickens = deepcopy(selected_chickens)
    new_chickens.append(idx)
    select_chicken(idx + 1, new_chickens)


select_chicken(0, [])

print(res)
