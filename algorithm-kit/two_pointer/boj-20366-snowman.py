# https://www.acmicpc.net/problem/20366
from sys import stdin, maxsize
from itertools import combinations

input = stdin.readline

N = int(input())
H = list(map(int, input().split()))
H = [(H[i], i) for i in range(len(H))]
combs = list(combinations(H, 2))
combs.sort(key=lambda h: h[0][0] + h[1][0])
min_result = maxsize

for i in range(len(combs) - 1):
    for j in range(i + 1, len(combs)):
        s = set()
        s.add(combs[i][0][1])
        s.add(combs[i][1][1])
        s.add(combs[j][0][1])
        s.add(combs[j][1][1])
        if len(s) != 4:
            continue

        diff = (combs[j][0][0] + combs[j][1][0]) - (combs[i][0][0] + combs[i][1][0])
        min_result = min(diff, min_result)

        break

print(min_result)
