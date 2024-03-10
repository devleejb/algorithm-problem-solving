from sys import stdin, maxsize

input = stdin.readline

N, M = map(int, input().split())
A = []

for _ in range(N):
    A.append(int(input()))

A.sort()

res = maxsize
end = 0

for start in range(N):
    while end < N:
        if A[end] - A[start] >= M:
            res = min(res, A[end] - A[start])
            break
        else:
            end += 1

print(res)
