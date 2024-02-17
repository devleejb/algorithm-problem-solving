# https://www.acmicpc.net/problem/1456
from sys import stdin
import math

input = stdin.readline

A, B = map(int, input().split())
sqrt_B = math.sqrt(B)
is_primes = [True] * (math.ceil(sqrt_B) + 1)
res = 0

for i in range(2, math.ceil(math.sqrt(sqrt_B)) + 1):
    if not is_primes[i]:
        continue

    j = 2
    while i * j <= sqrt_B:
        is_primes[i * j] = False
        j += 1

for i in range(2, math.ceil(sqrt_B) + 1):
    if not is_primes[i]:
        continue

    end = math.floor(math.log(B, i))
    start = max(2, math.ceil(math.log(A, i)))

    res += max(end - start + 1, 0)

print(res)