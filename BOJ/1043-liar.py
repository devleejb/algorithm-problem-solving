N, M = map(int, input().split())

truth = list(map(int, input().split()))[1:]
truth_group_leader = None
if len(truth) > 0:
    truth_group_leader = truth[0]


disjoint_set = [i for i in range(N + 1)]

for t in truth:
    disjoint_set[t] = truth_group_leader


def find_parent(a):
    if disjoint_set[a] != a:
        return find_parent(disjoint_set[a])
    return a


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        disjoint_set[b] = a
    elif a > b:
        disjoint_set[a] = b


parties = [list(map(int, input().split())) for _ in range(M)]

if truth_group_leader:
    for party in parties:
        members = party[1:]

        for i in range(len(members) - 1):
            union(members[i], members[i + 1])

    truth_leader = find_parent(truth_group_leader)

    res = 0

    for party in parties:
        members = party[1:]

        if len(members) > 0:
            parent = find_parent(members[0])

            if parent == truth_leader:
                res += 1

    print(M - res)
else:
    print(M)
