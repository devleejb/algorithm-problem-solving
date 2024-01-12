T = int(input())
t_list = [input().split() for _ in range(T)]

for t in t_list:
    cnt, word = t
    cnt = int(cnt)

    for c in word:
        for _ in range(cnt):
            print(c, end="")

    print()
