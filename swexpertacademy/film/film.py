from copy import deepcopy

def check_pass(films, K):
    width = len(films[0])
    height = len(films)

    for col in range(width):
        prev_cell = -1
        prev_cnt = 0
        success = False

        for row in range(height):
            if prev_cell == films[row][col]:
                prev_cnt += 1
            else:
                prev_cell = films[row][col]
                prev_cnt = 1
            if prev_cnt >= K:
                success = True
                break

        if not success:
            return False

    return True

res = 1234567890

def dfs(org_films, films, idx, K, cost):
    global res
    if check_pass(films, K):
        res = min(res, cost)

    if res <= cost:
        return

    if idx == len(films):
        return 1234567890

    dfs(org_films, films, idx + 1, K, cost)

    for i in range(2):
        films[idx] = [i] * len(films[0])
        dfs(org_films, films, idx + 1, K, cost + 1)
        films[idx] = org_films[idx]

T = int(input())

for test_case in range(1, T + 1):
    res = 1234567890
    D, W, K = map(int, input().split())
    films = [list(map(int, input().split())) for _ in range(D)]
    copied_films = deepcopy(films)
    dfs(copied_films, films, 0, K, 0)
    print("#" + str(test_case), res)
