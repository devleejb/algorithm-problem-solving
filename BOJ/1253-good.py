from bisect import bisect_left, bisect_right

N = int(input())
A = list(map(int, input().split()))

A.sort()

res = 0

for i, num in enumerate(A):
    # a + b == num
    for j, a in enumerate(A):
        if i == j:
            continue

        b = num - a
        left_idx = bisect_left(A, b)
        right_idx = bisect_right(A, b)

        if (num, a, b) == (0, 0, 0) and right_idx - left_idx < 3:
            continue

        if left_idx < len(A) and left_idx == right_idx - 1 and i == left_idx:
            continue

        if (a == b and left_idx + 1 < right_idx) or (a != b and left_idx != right_idx):
            res += 1
            break

print(res)
