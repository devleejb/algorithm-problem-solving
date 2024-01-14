num = input()
res_list = []

while num != "0":
    res = True
    for i in range(len(num) // 2):
        if num[i] != num[len(num) - i - 1]:
            res = False
            break
    res_list.append(res)
    num = input()


for res in res_list:
    if res:
        print("yes")
    else:
        print("no")
