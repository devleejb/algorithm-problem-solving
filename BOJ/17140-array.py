from sys import stdin
from collections import deque, Counter

input = stdin.readline

r, c, k = map(int, input().split())
r -= 1
c -= 1
array = [[0] * 100 for _ in range(100)]
q = deque([])

for row in range(3):
    items = list(map(int, input().split()))
    for col in range(3):
        array[row][col] = items[col]

q.append((array, 3, 3, 0))

res = -1

while q:
    array, row_cnt, col_cnt, cost = q.popleft()
    new_array = [[0] * 100 for _ in range(100)]

    if array[r][c] == k:
        res = cost
        break

    if cost == 100:
        break

    if row_cnt >= col_cnt:
        # R 연산
        max_col = 0
        for row in range(row_cnt):
            commons = sorted(
                Counter(array[row]).most_common(), key=lambda k: (k[1], k[0])
            )
            i = 0
            for num, cnt in commons:
                if num == 0:
                    continue
                new_array[row][i] = num
                i += 1
                new_array[row][i] = cnt
                i += 1

                if i >= 100:
                    break
            max_col = max(max_col, i)
        q.append((new_array, row_cnt, max_col, cost + 1))
    else:
        # C 연산
        max_row = 0
        for col in range(col_cnt):
            cols = []
            for row in range(row_cnt):
                cols.append(array[row][col])
            commons = sorted(Counter(cols).most_common(), key=lambda k: (k[1], k[0]))
            i = 0
            for num, cnt in commons:
                if num == 0:
                    continue
                new_array[i][col] = num
                i += 1
                new_array[i][col] = cnt
                i += 1

                if i >= 100:
                    break
            max_row = max(max_row, i)
        q.append((new_array, max_row, col_cnt, cost + 1))

print(res)
