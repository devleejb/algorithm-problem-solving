from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
routine = list(map(int, input().split()))
cnt = 0
using_tab = set([])

for i in range(len(routine)):
    if routine[i] in using_tab:
        pass
    elif len(using_tab) < N:
        using_tab.add(routine[i])
    else:
        max_idx = -1
        sliced = routine[i + 1 : len(routine)]
        is_resolved = False

        for tab in list(using_tab):
            if sliced.count(tab) > 0:
                max_idx = max(sliced.index(tab), max_idx)
            else:
                using_tab.remove(tab)
                using_tab.add(routine[i])
                cnt += 1
                is_resolved = True
                break
        if not is_resolved:
            using_tab.remove(routine[i + max_idx + 1])
            using_tab.add(routine[i])
            cnt += 1

print(cnt)
