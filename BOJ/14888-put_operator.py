from sys import stdin, maxsize

min_val = maxsize
max_val = -1234567890


def calc_val(A, O, result, idx):
    global min_val, max_val
    next_idx = idx + 1

    if idx == len(A):
        min_val = min(result, min_val)
        max_val = max(result, max_val)
        return

    for op_idx in range(len(O)):
        if O[op_idx] == 0:
            continue
        next_result = result

        if op_idx == 0:
            next_result += A[idx]
        elif op_idx == 1:
            next_result -= A[idx]
        elif op_idx == 2:
            next_result *= A[idx]
        else:
            if next_result < 0:
                next_result = -(abs(next_result) // A[idx])
            else:
                next_result //= A[idx]

        new_O = O.copy()
        new_O[op_idx] -= 1

        calc_val(A, new_O, next_result, next_idx)


input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
O = list(map(int, input().split()))

calc_val(A, O, A[0], 1)

print(max_val)
print(min_val)
