#include <stdio.h>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

int visited[20001];
int K, V, E, isBipartite;
vector<int> graph[20001];

void DFS(int vertex, vector<int>* graph, int visited[20001]) {
	int size = graph[vertex].size();
	
	if (isBipartite == 0) return;
	
	for (int i = 0; i < size; ++i) {
		int end = graph[vertex][i];
		
		if (visited[end] == 0) {
			visited[end] = (visited[vertex] % 2) + 1;
			
			DFS(end, graph, visited);
		} else if (visited[end] == visited[vertex]) {
			isBipartite = 0;
			
			return;
		}
	}
}


int main(void) {
	int start, end;
	
	scanf("%d", &K);
	
	for (int i = 0; i < K; ++i) {
		isBipartite = 1;
		
		scanf("%d %d", &V, &E);
		
		for (int j = 0; j < E; ++j) {
			scanf("%d %d", &start, &end);
		
			if (start == end) continue;
			
			graph[start].push_back(end);
			graph[end].push_back(start);
		}
		
		for (int j = 1; j <= V; ++j) {
			if (visited[j] == 0) {
				visited[j] = 1;
				DFS(j, graph, visited);
			} 
		}
		
		
		if (isBipartite == 1) printf("YES\n");
		else printf("NO\n");
		
		for (int j = 1; j <= V; ++j) {
			graph[j].clear();
		}
		
		memset(visited, 0, sizeof(visited));
	}
	
	return 0;
}