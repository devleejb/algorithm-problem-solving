from sys import stdin

input = stdin.readline

n = int(input())
changes = []

for _ in range(n):
    x, y = map(int, input().split())
    x -= 1
    changes.append((x, y))

changes.sort()

cnt = 0
active_floors = []

for x, y in changes:
    if not active_floors or active_floors[-1] < y:
        if y != 0:
            active_floors.append(y)
    else:
        while active_floors and active_floors[-1] > y:
            active_floors.pop()
            cnt += 1

        if y != 0 and (not active_floors or active_floors[-1] != y):
            active_floors.append(y)

if active_floors:
    cnt += len(active_floors)

print(cnt)
