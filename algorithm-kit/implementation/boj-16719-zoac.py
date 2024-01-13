# https://www.acmicpc.net/problem/16719
from sys import maxsize

word = list(input())
word_list = [[word[i], i] for i in range(len(word))]
pivot = sorted(word_list)[0][1]
used_list = [False for _ in word_list]
used_list[pivot] = True
selected_list = [pivot]

for _ in range(len(word_list) - 1):
    # 가장 오른쪽 토막에서 작은 것
    started = False
    min_val = [maxsize, 0]
    for j in reversed(range(pivot + 1, len(word_list))):
        if started == False and used_list[j]:
            continue
        if started and used_list[j]:
            break
        started = True

        min_val = min(min_val, [ord(word[j]), j])
    if min_val[0] != maxsize:
        used_list[min_val[1]] = True
        selected_list.append(min_val[1])
        continue

    # pivot 왼쪽에서 가장 가까운 토막에서 제일 작은 것
    started = False
    min_val = [maxsize, 0]
    for j in reversed(range(0, pivot)):
        if started == False and used_list[j]:
            continue
        if started and used_list[j]:
            break
        started = True

        min_val = min(min_val, [ord(word[j]), j])
    if min_val[0] != maxsize:
        used_list[min_val[1]] = True
        selected_list.append(min_val[1])

for i in range(len(selected_list)):
    to_show = selected_list[: i + 1]
    for idx in sorted(to_show):
        print(word[idx], end="")
    print()
