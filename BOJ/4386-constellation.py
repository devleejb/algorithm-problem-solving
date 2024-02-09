from sys import stdin
from itertools import combinations
import math

input = stdin.readline

n = int(input())
points = []
edges = []
disjoint_set = [i for i in range(n)]

for i in range(n):
    x, y = map(float, input().split())
    points.append((i, x, y))

combs = list(combinations(points, 2))

for comb in combs:
    a, b = comb
    distance = math.sqrt((a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)
    edges.append((distance, a[0], b[0]))

edges.sort()

def find_parent(a):
    if a != disjoint_set[a]:
        disjoint_set[a] = find_parent(disjoint_set[a])
        return disjoint_set[a]
    
    return a

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a > b:
        disjoint_set[a] = b
    else:
        disjoint_set[b] = a

res = 0

for cost, start, end in edges:
    parent_start = find_parent(start)
    parent_end = find_parent(end)

    if parent_start != parent_end:
        res += cost
        union(parent_start, parent_end)

print(res)
    


