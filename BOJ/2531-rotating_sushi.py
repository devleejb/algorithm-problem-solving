from sys import stdin

input = stdin.readline


def eat(eat_dict, sushi_num):
    if sushi_num not in eat_dict:
        eat_dict[sushi_num] = 0
    eat_dict[sushi_num] += 1


def subtract(eat_dict, sushi_num):
    eat_dict[sushi_num] -= 1
    if eat_dict[sushi_num] == 0:
        del eat_dict[sushi_num]


N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
sushi = sushi + sushi[:k]

eat_dict = {}
j = k - 1
result = 0

for i in range(k):
    eat(eat_dict, sushi[i])

while True:
    can_coupon = False

    if c not in eat_dict:
        can_coupon = True

    result = max(result, len(eat_dict) + (1 if can_coupon else 0))

    j += 1

    if j < len(sushi):
        eat(eat_dict, sushi[j])
        subtract(eat_dict, sushi[j - k])
    else:
        break


print(result)
