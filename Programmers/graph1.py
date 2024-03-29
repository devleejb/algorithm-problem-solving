from sys import maxsize
import heapq

def solution(n, edge):
    answer = 0
    edges = [[] for _ in range(n + 1)]
    dis = [maxsize] * (n + 1)
    visited = [False] * (n + 1)
    
    for start, end in edge:
        edges[start].append(end)
        edges[end].append(start)
        
    dis[1] = 0
    max_dis = 0
    
    hq = [(0, 1)]
    
    while hq:
        cost, node = heapq.heappop(hq)
        
        if visited[node]:
            continue
            
        visited[node] = True
        
        for end in edges[node]:
            if dis[end] > dis[node] + 1:
                dis[end] = dis[node] + 1
                heapq.heappush(hq, (dis[end], end))
                max_dis = max(max_dis, dis[end])
                
    for i in range(1, n + 1):
        if max_dis == dis[i]:
            answer += 1
    
    return answer