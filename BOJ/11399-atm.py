N = int(input())
P = list(map(int, input().split()))

P.sort()
result = P[0]

for i in range(1, N):
    P[i] += P[i - 1]
    result += P[i]

print(result)
