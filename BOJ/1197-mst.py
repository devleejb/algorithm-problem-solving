from sys import stdin

input = stdin.readline
parent_list = list(range(10_001))


def union_parent(a, b):
    parent_a = find_parent(a)
    parent_b = find_parent(b)
    if parent_a > parent_b:
        parent_list[parent_a] = parent_b
    else:
        parent_list[parent_b] = parent_a


def find_parent(a):
    if a == parent_list[a]:
        return a
    return find_parent(parent_list[a])


V, E = map(int, input().split())
edge_list = []
min_cost = 0

for _ in range(E):
    start, end, cost = map(int, input().split())
    edge_list.append((cost, start, end))

edge_list.sort()

for edge in edge_list:
    cost, start, end = edge

    if find_parent(start) != find_parent(end):
        union_parent(start, end)
        min_cost = min_cost + cost

print(min_cost)
