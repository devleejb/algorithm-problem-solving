# https://www.acmicpc.net/problem/1647
from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
edges = []
disjoint_set = [i for i in range(N)]

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

for _ in range(M):
    start, end, cost = map(int, input().split())
    start -= 1
    end -= 1
    edges.append((cost, start, end))

edges.sort()

res = 0
last_cost = 0
for cost, start, end in edges:
    parent_start = find_parent(start)
    parent_end = find_parent(end)

    if parent_start != parent_end:
        res += cost
        last_cost = cost
        union(parent_start, parent_end)

res -= last_cost

print(res)