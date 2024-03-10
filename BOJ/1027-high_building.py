from sys import stdin, maxsize

input = stdin.readline

N = int(input())
buildings = list(map(int, input().split()))
res = 0

for i, height in enumerate(buildings):
    cnt = 0
    min_slope = maxsize
    arr = []
    # left
    for j in reversed(range(i)):
        slope = (height - buildings[j]) / (i - j)
        if slope < min_slope:
            min_slope = slope
            cnt += 1
            arr.append(j)
    # right
    max_slope = -maxsize
    for j in range(i + 1, N):
        slope = (buildings[j] - height) / (j - i)
        if slope > max_slope:
            max_slope = slope
            cnt += 1
            arr.append(j)

    res = max(res, cnt)

print(res)
