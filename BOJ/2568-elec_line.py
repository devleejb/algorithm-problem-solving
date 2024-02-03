from sys import stdin
import bisect

input = stdin.readline

N = int(input())
lines = []
A_lines = []
lis = []
record = [0] * N

for _ in range(N):
    A, B = map(int, input().split())
    lines.append([B, A])

lines.sort()

for i, (B, A) in enumerate(lines):
    A_lines.append((A, i))

A_lines.sort()

lis.append(A_lines[0][1])
record[0] = 1

for i, A_line in enumerate(A_lines[1:]):
    i += 1
    a = bisect.bisect_left(lis, A_line[1])

    if a == len(lis):
        lis.append(A_line[1])
        record[i] = len(lis)
    else:
        lis[a] = A_line[1]
        record[i] = a + 1

print(N - len(lis))
target = len(lis)
delete_targets = []
i = N - 1
while i >= 0:
    if target == record[i]:
        target -=1
    else:
        delete_targets.append(A_lines[i][0])
    i -= 1

delete_targets.sort()
for target in delete_targets:
    print(target)