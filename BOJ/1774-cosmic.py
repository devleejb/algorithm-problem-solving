from itertools import combinations
from sys import stdin
from math import sqrt
import heapq

input = stdin.readline

N, M = map(int, input().split())
sets = [i for i in range(N)]

positions = [[i, list(map(int, input().split()))] for i in range(N)]
connected = [list(map(int, input().split())) for _ in range(M)]


def find_parent(a):
    if a != sets[a]:
        sets[a] = find_parent(sets[a])
    return sets[a]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a > b:
        sets[a] = b
    elif a < b:
        sets[b] = a


for a, b in connected:
    union(a - 1, b - 1)

combs = list(combinations(positions, 2))
hq = []

for a, b in combs:
    a_idx, a_pos = a
    b_idx, b_pos = b
    a_parent = find_parent(a_idx)
    b_parent = find_parent(b_idx)

    if a_parent == b_parent:
        continue

    dis = sqrt((a_pos[0] - b_pos[0]) ** 2 + (a_pos[1] - b_pos[1]) ** 2)

    heapq.heappush(hq, (dis, a_idx, b_idx))

res = 0

while hq:
    dis, a_idx, b_idx = heapq.heappop(hq)
    a_parent = find_parent(a_idx)
    b_parent = find_parent(b_idx)

    if a_parent == b_parent:
        continue

    res += dis

    union(a_parent, b_parent)

print("{:.2f}".format(res))
