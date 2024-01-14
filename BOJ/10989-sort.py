from sys import stdin

input = stdin.readline

N = int(input())
table = [0] * 10_001

for _ in range(N):
    num = int(input())
    table[num] += 1

for i, cnt in enumerate(table):
    for _ in range(cnt):
        print(i)
