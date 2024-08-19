S, K = map(int, input().split())
seq = list(map(int, input().split()))

j = 0
max_len = 0
cur_len = 0
skipped = 0
for i in range(S):
    while j < S:
        if seq[j] % 2 == 0:
            j += 1
            cur_len += 1
            max_len = max(max_len, cur_len)
        elif skipped < K:
            j += 1
            skipped += 1
        else:
            if seq[i] % 2 == 1:
                skipped -= 1
            else:
                cur_len -= 1
            break

print(max_len)
