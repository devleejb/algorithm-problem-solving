import heapq


def solution(prices):
    answer = [0] * len(prices)
    hq = []

    for i, price in enumerate(prices):
        while hq and -hq[0][0] > price:
            _, popped_i = heapq.heappop(hq)
            answer[popped_i] = i - popped_i

        heapq.heappush(hq, (-price, i))

    while hq:
        _, popped_i = heapq.heappop(hq)
        answer[popped_i] = i - popped_i

    return answer
