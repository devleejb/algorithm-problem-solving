N = int(input())

cnt_5 = N // 5
cnt_3 = (N - 5 * cnt_5) // 3
remain = N - cnt_5 * 5 - cnt_3 * 3

while remain > 0:
    if cnt_5 <= 0:
        break
    cnt_5 -= 1
    cnt_3 = (N - 5 * cnt_5) // 3
    remain = N - cnt_5 * 5 - cnt_3 * 3


if remain == 0:
    print(cnt_5 + cnt_3)
else:
    print(-1)
