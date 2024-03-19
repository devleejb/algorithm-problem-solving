import heapq

N = int(input())
cards = [int(input()) for _ in range(N)]
heapq.heapify(cards)

res = 0

while cards:
    card1 = heapq.heappop(cards)

    if cards:
        card2 = heapq.heappop(cards)

        cost = card1 + card2
        res += cost

        heapq.heappush(cards, cost)
    else:
        print(res)
