#include <stdio.h>
#include <queue>
#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int N, M;
int visited[2000];
vector<int> graph[2000];

void DFS(int* visited, int now, int level) {
	if (level == 5) {
		printf("1");
		
		exit(0);
	}
	
	for (int i = 0; i < graph[now].size(); ++i) {
		if (visited[graph[now][i]] == 0) {
			visited[graph[now][i]] = 1;
			DFS(visited, graph[now][i], level + 1);
			visited[graph[now][i]] = 0;
		}
	}
}

int main(void) {
	int start, end;
	
	scanf("%d %d", &N, &M);
	
	for (int i = 0; i < M; ++i) {
		scanf("%d %d", &start, &end);
		
		graph[start].push_back(end);
		graph[end].push_back(start);
	}
	
	for (int i = 0; i < N; ++i) {
		visited[i] = 1;
		
		DFS(visited, i, 1);
		
		memset(visited, 0, sizeof(visited));
	}
	
	printf("0");
	
	return 0;
}