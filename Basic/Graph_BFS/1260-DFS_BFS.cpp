#include <stdio.h>
#include <queue>

using namespace std;

int N, M, V;
int graph[1001][1001];
int visited_BFS[1001];
int visited_DFS[1001];

void BFS() {
	int nowVer;
	queue<int> q;
	
	q.push(V);
	visited_BFS[V] = 1;
	
	while (!q.empty()) {
		nowVer = q.front();
		q.pop();
		
		printf("%d ", nowVer);
		
		for (int i = 1; i <= N; ++i) {
			if (graph[nowVer][i] && !visited_BFS[i]) {
				q.push(i);
				visited_BFS[i] = 1;
			}
		}
	}
}

void DFS(int nowVer) {
	visited_DFS[nowVer] = 1;
	printf("%d ", nowVer);
	
	for (int i = 1; i <= N; ++i) {
		if (graph[nowVer][i] && !visited_DFS[i]) {
			DFS(i);
		}
	}
}

int main(void) {
	int ver1, ver2;
	
	scanf("%d %d %d", &N, &M, &V);
	
	for (int i = 0; i < M; ++i) {
		scanf("%d %d", &ver1, &ver2);
		
		graph[ver1][ver2] = graph[ver2][ver1] = 1;
	}
	
	DFS(V);
	
	printf("\n");
	
	BFS();
	
	return 0;
} 