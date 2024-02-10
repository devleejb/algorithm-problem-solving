from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

input = stdin.readline


def find_parent(disjoint_set, a):
    if a != disjoint_set[a]:
        disjoint_set[a] = find_parent(disjoint_set, disjoint_set[a])
        return disjoint_set[a]

    return a

def union(disjoint_set, a, b):
    a = find_parent(disjoint_set, a)
    b = find_parent(disjoint_set, b)

    if a > b:
        disjoint_set[b] = a
    else:
        disjoint_set[a] = b

res_list = []

while True:
    M, N = map(int, input().split())

    if M == 0 and N == 0:
        break

    edges = []
    disjoint_set = [i for i in range(M)]
    total_cost = 0

    for _ in range(N):
        start, end, cost = map(int, input().split())
        edges.append((cost, start, end))
        total_cost += cost

    edges.sort()

    for cost, start, end in edges:
        parent_start = find_parent(disjoint_set, start)
        parent_end = find_parent(disjoint_set, end)

        if parent_start != parent_end:
            union(disjoint_set, parent_start, parent_end)
            total_cost -= cost

    res_list.append(total_cost)

for res in res_list:
    print(res)

