from collections import deque

T = int(input())
results = []
n = 9999
a = [False, False] + [True] * (n - 1)
primes = {}

for i in range(2, n + 1):
    if a[i]:
        if (i >= 1000):
            primes[str(i)] = True
        for j in range(2 * i, n + 1, i):
            a[j] = False


def is_prime(number):
    return number in primes


for i in range(T):
    visited = {}
    from_pass, to_pass = input().split()

    queue = deque([from_pass])
    visited[from_pass] = 0

    while queue:
        password = queue.popleft()

        for i in range(len(password)):
            for number in range(10):
                next_pass = list(password)
                next_pass[i] = str(number)
                next_pass = "".join(next_pass)

                if (is_prime(next_pass) and not (next_pass in visited)):
                    visited[next_pass] = visited[password] + 1
                    queue.append(next_pass)

    if (to_pass in visited):
        results.append(visited[to_pass])
    else:
        results.append("Impossible")

for result in results:
    print(result)
