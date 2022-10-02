K, N = map(int, input().split())
utp_list = []

for i in range(K):
    utp_list.append(int(input()))


def can_make_utp(length):
    count = 0

    for utp in utp_list:
        count += utp // length

    return count >= N


start = 1
end = max(utp_list)
max_len = 0

while start <= end:
    mid = (start + end) // 2

    if (can_make_utp(mid)):
        max_len = mid
        start = mid + 1
    else:
        end = mid - 1

print(max_len)
