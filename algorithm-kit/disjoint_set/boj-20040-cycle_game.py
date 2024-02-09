# https://www.acmicpc.net/problem/20040
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

input = stdin.readline

n, m = map(int, input().split())
disjoint_set = [i for i in range(n)]

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

res = 0

for i in range(m):
    a, b = map(int, input().split())
    parent_a = find_parent(a)
    parent_b = find_parent(b)

    if parent_a == parent_b:
        res = i + 1
        break
    
    union(parent_a, parent_b)

print(res)
