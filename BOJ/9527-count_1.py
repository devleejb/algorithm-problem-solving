from sys import stdin

input = stdin.readline

A, B = map(int, input().split())
cnts = [0] * 56

cnts[1] = 1
cnts[2] = 4
cnts[3] = 12

for i in range(4, 56):
    cnts[i] = 2 * cnts[i - 1] + (2 ** (i - 1))


def count(bin_num):
    bin_num_len = len(bin_num) - 2
    num = int(bin_num, 2)

    if num == 0:
        return 0
    elif num == 1:
        return 1

    return (
        (num - (2 ** (bin_num_len - 1) - 1))
        + cnts[bin_num_len - 1]
        + count(bin(num - 2 ** (bin_num_len - 1)))
    )


print(count(bin(B)) - count(bin(A - 1)))
