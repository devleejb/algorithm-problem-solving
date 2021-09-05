#include <stdio.h>

using namespace std;

int N, M;
int graph[1001][1001];
int visited[1001];

void DFS(int vertex) {
	visited[vertex] = 1;
	
	for (int i = 1; i <= N; ++i) {
		if (graph[vertex][i] && !visited[i]) {
			DFS(i);
		}
	}
}

int main(void) {
	int u, v;
	int cnt = 0;
	
	scanf("%d %d", &N, &M);
	
	for (int i = 0; i < M; ++i) {
		scanf("%d %d", &u, &v);
		
		graph[u][v] = graph[v][u] = 1;
	}
	
	for (int i = 1; i <= N; ++i) {
		if (!visited[i]) {
			++cnt;
			DFS(i);
		}
	}
	
	printf("%d", cnt);
	
	return 0;
}