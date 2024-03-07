from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

input = stdin.readline

N = int(input())
villages = list(map(int, input().split()))
visited = [False] * N
dp = [[0, 0] for _ in range(N)]
edges = [[] for _ in range(N)]
NORMAL_VILLAGE = 0
GOOD_VILLAGE = 1

for _ in range(N - 1):
    start, end = map(int, input().split())
    start -= 1
    end -= 1
    edges[start].append(end)
    edges[end].append(start)


def dfs(village):
    visited[village] = True
    dp[village][GOOD_VILLAGE] = villages[village]

    for to in edges[village]:
        if visited[to]:
            continue

        dfs(to)
        dp[village][GOOD_VILLAGE] += dp[to][NORMAL_VILLAGE]
        dp[village][NORMAL_VILLAGE] += max(dp[to])

    return max(dp[village])


print(dfs(0))
