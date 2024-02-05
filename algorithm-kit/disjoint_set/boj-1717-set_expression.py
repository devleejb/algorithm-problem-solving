# https://www.acmicpc.net/problem/1717
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

input = stdin.readline

n, m = map(int, input().split())
sets = [i for i in range(n + 1)]

def find(a):
    if a != sets[a]:
        sets[a] = find(sets[a])

        return sets[a]

    return a

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        sets[b] = a
    else:
        sets[a] = b


res_list = []

for _ in range(m):
    op, a, b = map(int, input().split())

    if op == 0:
        union(a, b)
    elif op == 1:
        a_parent = find(a)
        b_parent = find(b)

        if a_parent == b_parent:
            res_list.append("YES")
        else:
            res_list.append("NO")

for res in res_list:
    print(res)
