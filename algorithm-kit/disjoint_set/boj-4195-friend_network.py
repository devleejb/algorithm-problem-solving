# https://www.acmicpc.net/problem/4195
from sys import stdin

input = stdin.readline


def find_parent(network, network_cnt, a):
    if network.get(a) == None or network[a] == a:
        if network.get(a) == None:
            network[a] = a
            network_cnt[a] = 1
        return a
    
    network[a] = find_parent(network, network_cnt, network[a])
    return network[a]

def union(network, network_cnt, a, b):
    a = find_parent(network, network_cnt, a)
    b = find_parent(network, network_cnt, b)

    if a > b:
        network[a] = b
        network_cnt[b] += network_cnt[a]
        return b
    elif a < b:
        network[b] = a
        network_cnt[a] += network_cnt[b]
        return a
    else:
        return a

T = int(input())

for _ in range(T):
    F = int(input())
    network = {}
    network_cnt = {}

    for _ in range(F):
        a, b = input().split()

        parent = union(network, network_cnt, a, b)
        print(network_cnt[parent])

