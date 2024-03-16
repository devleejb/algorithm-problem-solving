from sys import stdin

input = stdin.readline

N, C = map(int, input().split())
homes = [int(input()) for _ in range(N)]
homes.sort()

start = 1
end = homes[N - 1] - homes[0]

while start <= end:
    mid = (start + end) // 2
    prev = 0
    cnt = 1

    for i in range(1, N):
        if homes[i] - homes[prev] >= mid:
            prev = i
            cnt += 1

    if cnt < C:
        end = mid - 1
    else:
        start = mid + 1

print(start - 1)
