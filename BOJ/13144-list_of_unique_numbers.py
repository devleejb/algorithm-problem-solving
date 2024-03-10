from sys import stdin

input = stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
visited = [False] * 100_001


def run():
    res = 0
    end = 0

    for start in range(N):
        while end < N:
            if visited[numbers[end]]:
                visited[numbers[start]] = False
                break
            else:
                visited[numbers[end]] = True
                end += 1
                res += end - start

    print(res)


run()
