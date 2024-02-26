from sys import stdin

input = stdin.readline

N, M, K = map(int, input().split())
plants = list(map(int, input().split()))
edges = []
disjoint_set = [i for i in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))
edges.sort()


def find_parent(a):
    if a != disjoint_set[a]:
        disjoint_set[a] = find_parent(disjoint_set[a])
        return disjoint_set[a]

    return disjoint_set[a]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a in plants:
        disjoint_set[b] = a
    else:
        disjoint_set[a] = b


res = 0

for cost, start, end in edges:
    start_parent = find_parent(start)
    end_parent = find_parent(end)

    if start_parent in plants and end_parent in plants:
        continue

    if start_parent != end_parent:
        union(start_parent, end_parent)
        res += cost

print(res)
