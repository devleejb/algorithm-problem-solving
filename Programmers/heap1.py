import heapq

def solution(scoville, K):
    answer = 0
    hq = []
    
    for sc in scoville:
        heapq.heappush(hq, sc)
        
    cnt = 0
    while hq:    
        sc1 = heapq.heappop(hq)
        
        if sc1 >= K:
            answer = cnt
            break
            
        cnt += 1

        if not hq:
            answer = -1
            break
            
        sc2 = heapq.heappop(hq)
        
        new_sc = sc1 + 2 * sc2
        
        heapq.heappush(hq, new_sc)
            
    if answer != -1:
        answer = cnt
    
    
    return answer