CREATE = "100"
EAT = "111"
ENTER = "200"
OUT = "222"
PIC = "300"

L, Q = map(int, input().split())
queries = []
sushi_by_name = {}
customer_pos = {}
res_list = []

for _ in range(Q):
    query = input().split()
    op = query[0]
    t = int(query[1])
    queries.append((t, query))

    if op == CREATE:
        pos = int(query[2])
        name = query[3]
        if name not in sushi_by_name:
            sushi_by_name[name] = []
        sushi_by_name[name].append((t, pos))
    elif op == ENTER:
        pos = int(query[2])
        name = query[3]
        remain_cnt = int(query[4])
        customer_pos[name] = (t, pos, remain_cnt)

for name in customer_pos.keys():
    enter_time, cus_pos, remain_cnt = customer_pos[name]
    exit_time = 0
    customer_pos[name] = -1

    for made_time, sushi_pos in sushi_by_name[name]:
        if made_time > enter_time:
            pos_diff = (cus_pos - sushi_pos + L) % L
            exit_time = made_time + pos_diff
            queries.append((made_time + pos_diff, [EAT]))
        elif made_time < enter_time:
            sushi_pos_in_enter_time = (sushi_pos + (enter_time - made_time)) % L
            pos_diff = (cus_pos - sushi_pos_in_enter_time + L) % L
            exit_time = enter_time + pos_diff
            queries.append((enter_time + pos_diff, [EAT]))
        customer_pos[name] = max(customer_pos[name], exit_time)

for name in customer_pos.keys():
    queries.append((customer_pos[name], [OUT]))

queries.sort(key=lambda k: (k[0], k[1][0]))

sushi_len = 0
people_len = 0

for time, query in queries:
    op = query[0]

    if op == CREATE:
        sushi_len += 1
    elif op == EAT:
        sushi_len -= 1
    elif op == ENTER:
        people_len += 1
    elif op == OUT:
        people_len -= 1
    else:
        print(people_len, sushi_len)
