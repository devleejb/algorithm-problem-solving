A, B, C = map(int, input().split())


def f(A, B):
    if B == 1:
        return A % C

    if B % 2 == 0:
        return (f(A, B // 2) ** 2) % C
    else:
        return ((f(A, B // 2) ** 2) * A) % C


print(f(A, B))
