from sys import stdin, maxsize

input = stdin.readline

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))

A.sort()

min_sum = maxsize
min_val = None

i = 0
j = N - 1

while i < j:
    sum = A[i] + A[j]

    if abs(sum) < min_sum:
        min_sum = abs(sum)
        min_val = (A[i], A[j])

    if sum < 0:
        i += 1
    elif sum > 0:
        j -= 1
    else:
        break

print(*min_val)
