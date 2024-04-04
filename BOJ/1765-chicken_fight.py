from sys import stdin

input = stdin.readline

n = int(input())
m = int(input())
friends = [[0] * n for _ in range(n)]
enemies = [[0] * n for _ in range(n)]
sets = [i for i in range(n)]


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


for _ in range(m):
    type, a, b = input().rstrip().split()
    a = int(a) - 1
    b = int(b) - 1

    if type == "F":
        friends[a][b] = 1
        friends[b][a] = 1
    elif type == "E":
        enemies[a][b] = 1
        enemies[b][a] = 1

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if friends[i][j]:
            union(i, j)
        if enemies[i][j]:
            for k in range(n):
                if enemies[j][k]:
                    union(i, k)

print(len(set(sets)))
