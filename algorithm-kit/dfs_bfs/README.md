## DFS이란?

- 깊은 부분을 우선적으로 탐색하는 알고리즘
- Stack(또는 Recursion)을 이용하여 구현

## DFS 동작 과정

1. 탐색 시작 노드를 스택에 삽입하고 방문처리 한다.
2. 스택의 최상단에 방문하지 않은 인접한 노드가 있다면, **그 노드**를 스택에 넣고 방문처리한다. 방문처리하지 않은 인접 노드가 없다면 스택에서 최상단 노드를 꺼낸다.
3. 2번을 수행할 수 없을 때까지 반복한다.

## DFS 소스 코드

```python
def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
```

## BFS란?

- **가까운 노드부터 우선적**으로 탐색하는 알고리즘
- Queue를 이용하여 구현한다.
- 최단경로 찾기에 사용할 수 있다.

## BFS 동작 과정

1. 탐색 시작 노드를 큐에 삽입하고 방문처리한다.
2. 큐에서 노드를 꺼낸 뒤에 해당하는 노드의 인접 노드 중에서 방문하지 않은 **모든 노드**를 큐에 삽입하고 방문처리한다.
3. 2번을 수행할 수 없을 때까지 반복한다.

## BFS 소스 코드

```python
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
```

## 참고 자료

- [(이코테 2021 강의 몰아보기) 3. DFS & BFS](https://youtu.be/7C9RgOcvkvo?si=LUU15k_SGyuyeHVu)
