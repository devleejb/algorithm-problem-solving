from sys import stdin, setrecursionlimit

setrecursionlimit(10**7)

input = stdin.readline

T = int(input())

VISITED = 2
VISITING = 1
NOT_VISITED = 0


def dfs(student, affinities, visited, prev, matched):
    visited[student] = VISITING
    next_student = affinities[student]

    if visited[next_student] == VISITING:
        track_student = student
        matched[track_student] = True
        while track_student != next_student:
            track_student = prev[track_student]
            matched[track_student] = True
    elif visited[next_student] == NOT_VISITED:
        prev[next_student] = student
        dfs(next_student, affinities, visited, prev, matched)

    visited[student] = VISITED

    return visited


res_list = []

for _ in range(T):
    N = int(input())
    affinities = list(map(int, input().split()))
    visited = [NOT_VISITED] * N
    prev = [-1] * N
    matched = [False] * N

    for i, affinity in enumerate(affinities):
        affinities[i] -= 1

    for student in range(N):
        if visited[student] != NOT_VISITED:
            continue
        visited = dfs(student, affinities, visited, prev, matched)

    cnt = 0
    for match in matched:
        if not match:
            cnt += 1
    res_list.append(cnt)

for res in res_list:
    print(res)
