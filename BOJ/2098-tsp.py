from sys import maxsize

N = int(input())
edges = [list(map(int, input().split())) for _ in range(N)]
visited_cost = [[-1 for _ in range(2**N)] for _ in range(N)]
START_CITY = 0
ALL_VISIT = 2**N - 1


def visit(city, visited_bit):
    if city == START_CITY and visited_bit == ALL_VISIT:
        return 0

    if visited_cost[city][visited_bit] != -1:
        return visited_cost[city][visited_bit]

    visited_cost[city][visited_bit] = maxsize

    for to_city, edge_cost in enumerate(edges[city]):
        if edge_cost == 0 or visited_bit & 1 << to_city != 0:
            continue
        next_visited_bit = visited_bit | 1 << to_city

        if to_city != START_CITY or visited_bit == 2**N - 2:
            res = visit(to_city, next_visited_bit)
            visited_cost[city][visited_bit] = min(
                visited_cost[city][visited_bit], res + edge_cost
            )

    return visited_cost[city][visited_bit]


print(visit(START_CITY, 0))
