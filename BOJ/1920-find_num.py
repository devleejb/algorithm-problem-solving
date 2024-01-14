N = int(input())
n_list = list(map(int, input().split()))
M = int(input())
m_list = list(map(int, input().split()))

dict_obj = {}

for n in n_list:
    dict_obj[n] = True

for m in m_list:
    print(int(m in dict_obj))
