from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
names = input().split()
names.sort()
indegrees = {}
graph = {}
reverse_graph = {}
parent_found = {}
childs = {}

for name in names:
    indegrees[name] = 0
    graph[name] = []
    reverse_graph[name] = []
    childs[name] = []
    parent_found[name] = False

M = int(input())

for _ in range(M):
    X, Y = input().split()
    indegrees[Y] += 1
    graph[X].append(Y)
    reverse_graph[Y].append(X)

q = deque([])

for name in indegrees:
    if indegrees[name] != 0:
        continue

    q.appendleft(name)

while q:
    name = q.popleft()

    for from_name in reverse_graph[name]:
        if parent_found[from_name]:
            continue
        childs[name].append(from_name)
        parent_found[from_name] = True

    for to_name in graph[name]:
        indegrees[to_name] -= 1

        if indegrees[to_name] == 0:
            q.appendleft(to_name)

ancestors = []
res_list = []

for name in names:
    res_list.append((name, len(childs[name]), sorted(childs[name])))
    if not parent_found[name]:
        ancestors.append(name)

print(len(ancestors))
print(*ancestors)
for name, child_len, childs in res_list:
    print(name, child_len, *childs)
