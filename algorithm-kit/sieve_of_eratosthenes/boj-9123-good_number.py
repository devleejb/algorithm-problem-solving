# https://www.acmicpc.net/problem/9213
from sys import stdin
import math

input = stdin.readline

res_list = []
start, stop, badness = map(int, input().split())

while not (start == 0 and stop == 0 and badness == 0):
    sqrt_stop = math.sqrt(stop)
    summed_factors = [1] * (stop + 1)
    summed_factors[0] = 0
    summed_factors[0] = 1

    for i in range(2, math.floor(sqrt_stop) + 1):
        j = 2

        while i * j <= stop:
            summed_factors[i * j] += i
            if j > math.floor(sqrt_stop):
                summed_factors[i * j] += j
            j += 1

    res = 0
    for i in range(start, stop + 1):
        if abs(summed_factors[i] - i) <= badness:
            res += 1

    res_list.append(res)
    start, stop, badness = map(int, input().split())

for i, res in enumerate(res_list):
    print(f"Test {i + 1}: {res}")
