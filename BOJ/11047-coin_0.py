N, K = map(int, input().split())

coinList = []
result = 0

# 코인 종류 입력
for i in range(0, N):
    coinList.append(int(input()))

for i in range(0, N):
    count = K // coinList[N - i - 1]
    result += count
    K -= count * coinList[N - i - 1]

    if (K == 0):
        break

print(result)
