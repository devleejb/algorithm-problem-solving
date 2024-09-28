def safe_get(arr, idx):
    if idx < 0 or len(arr) <= idx:
        return 0
    return arr[idx]


def sol(a):
    b = []
    for i in range(len(a)):
        b.append(safe_get(a, i - 1) + safe_get(a, i) + safe_get(a, i + 1))
    return b


print(sol([4, 0, 1, -2, 3]))
