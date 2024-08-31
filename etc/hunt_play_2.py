# https://youtu.be/t7z1CjN0MBY?si=kxgxnFB6MTLnaUIP

dir_list = list(input())
dir_len = len(dir_list)

sum = 0
inc = []

for i, dir in enumerate(dir_list):
    left_cnt = i
    right_cnt = dir_len - i - 1

    if dir == "L":
        sum += left_cnt
    else:
        sum += right_cnt

    if dir == "L" and right_cnt > left_cnt:
        inc.append(right_cnt - left_cnt)
    elif dir == "R" and left_cnt > right_cnt:
        inc.append(left_cnt - right_cnt)

inc.sort(reverse=True)

for i in range(dir_len):
    if len(inc) > i:
        sum += inc[i]
    print(sum, end=" ")
