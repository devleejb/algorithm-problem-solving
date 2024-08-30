from collections import deque


def bfs():
    C, B = map(int, input().split())
    q = deque([B])
    time = 0

    while True:
        C += time
        next_q = deque([])

        if C > 200_000:
            return -1

        while q:
            b = q.popleft()

            if b == C:
                return time

            next_q.append(b - 1)
            next_q.append(b + 1)
            next_q.append(b * 2)

        q = next_q

        time += 1


print(bfs())
