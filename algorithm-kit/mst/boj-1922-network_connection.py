# https://www.acmicpc.net/problem/1922
from sys import stdin

input = stdin.readline

N = int(input())
M = int(input())
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
        disjoint_set[b] = a
    else:
        disjoint_set[a] = b

for _ in range(M):
    start, end, cost = map(int, input().split())
    start -= 1
    end -= 1
    edges.append((cost, start, end))

edges.sort()

res = 0

for cost, start, end in edges:
    parent_start = find_parent(start)
    parent_end = find_parent(end)

    if parent_start != parent_end:
        union(parent_start, parent_end)
        res += cost

print(res)

