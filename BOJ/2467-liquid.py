from sys import stdin, maxsize

input = stdin.readline

N = int(input())
liquids = list(map(int, input().split()))
liquids.sort()


min_val = maxsize
res = [0, 0]
start = 0
end = N - 1
visited = [False] * (N + 1)

while start < end:
    summed_val = liquids[start] + liquids[end]
    if abs(summed_val) < min_val:
        min_val = abs(summed_val)
        res = [liquids[start], liquids[end]]

    if summed_val < 0:
        if not visited[start + 1]:
            start += 1
            visited[start] = True
        else:
            break
    elif summed_val > 0:
        if not visited[end - 1]:
            end -= 1
            visited[end] = True
        else:
            break
    else:
        break


print(*res)

    