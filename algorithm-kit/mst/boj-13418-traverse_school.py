# https://www.acmicpc.net/problem/13418
from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
edges = []

def find_parent(disjoint_set, a):
    if a != disjoint_set[a]:
        disjoint_set[a] = find_parent(disjoint_set, disjoint_set[a])
        return disjoint_set[a]
    
    return a

def union(disjoint_set, a, b):
    a = find_parent(disjoint_set, a)
    b = find_parent(disjoint_set, b)

    if a > b:
        disjoint_set[a] = b
    else:
        disjoint_set[b] = a

def mst(edges):
    cnt = 0
    disjoint_set = [i for i in range(N + 1)]

    for type, start, end in edges:
        parent_start = find_parent(disjoint_set, start)
        parent_end = find_parent(disjoint_set, end)

        if parent_start != parent_end:
            union(disjoint_set, parent_start, parent_end)

            if type == 0:
                cnt += 1

    return cnt ** 2


for _ in range(M + 1):
    start, end, type = map(int, input().split())
    edges.append((type, start, end))

edges.sort()

print(mst(edges) - mst(reversed(edges)))


