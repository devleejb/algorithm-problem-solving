from sys import stdin
from collections import deque

input = stdin.readline
q = deque()

bracket_str = list(input().strip())

try:
    for b in bracket_str:
        if b == "(" or b == "[":
            q.append(b)
        else:
            if len(q) == 0:
                break
            top = q.pop()
            local_result = 0

            while len(q) > 0 and isinstance(top, int):
                local_result += top
                top = q.pop()

            local_result = 1 if local_result == 0 else local_result

            if top == "(" and b == ")":
                local_result *= 2
            elif top == "[" and b == "]":
                local_result *= 3
            else:
                raise Exception()

            q.append(local_result)

    result = 0

    for val in q:
        if isinstance(val, int):
            result += val
        else:
            raise Exception()

    print(result)
except:
    print(0)
