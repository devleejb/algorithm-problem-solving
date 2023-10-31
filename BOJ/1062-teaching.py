from sys import stdin
from itertools import combinations

input = stdin.readline

N, K = map(int, input().split())
words = [input() for _ in range(N)]


def calc_readable_words(alphabets):
    cnt = 0
    for word in words:
        is_readable = True
        chrs = list(word)
        for c in chrs[4 : len(chrs) - 5]:
            if c not in alphabets:
                is_readable = False
                break
        if is_readable:
            cnt += 1
    return cnt


def calc_max_readable_words():
    if K < 5:
        return 0
    result = 0
    candidate_alphabets = []
    fixed_alphabets = ["a", "n", "t", "i", "c"]

    for i in range(26):
        candidate_chr = chr(ord("a") + i)

        if candidate_chr not in fixed_alphabets:
            candidate_alphabets.append(candidate_chr)

    combs = list(combinations(candidate_alphabets, K - 5))

    for comb in combs:
        result = max(calc_readable_words(fixed_alphabets + list(comb)), result)

    return result


print(calc_max_readable_words())
