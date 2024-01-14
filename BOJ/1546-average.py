N = int(input())
num_list = list(map(int, input().split()))

max_val = max(num_list)

for i in range(len(num_list)):
    num = num_list[i]
    num_list[i] = num / max_val * 100

print(sum(num_list) / len(num_list))
