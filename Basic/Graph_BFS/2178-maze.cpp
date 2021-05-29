#include <stdio.h>
#include <iostream>
#include <string>
#include <queue>
#include <vector>

using namespace std;

int N, M;
int maze[101][101];
int visited[101][101];
int dxdy[4][2] = {
	{-1, 0},
	{0, 1},
	{1, 0},
	{0, -1}
};

int isMovable(int row, int col) {
	if (row > 0 && row <= N && col > 0 && col <= M && visited[row][col] == 0 && maze[row][col] == 1) return 1;
	else return 0;
}

int BFS() {
	queue<int> rq, cq, disq;
	int row, col, newRow, newCol, dis;
	
	visited[1][1] = 1;
	rq.push(1);
	cq.push(1);
	disq.push(1);
	
	while (!rq.empty()) {
		row = rq.front();
		col = cq.front();
		dis = disq.front();
		
		rq.pop();
		cq.pop();
		disq.pop();
		
		if (row == N && col == M) return dis;
		
		for (int i = 0; i < 4; ++i) {
			newRow = row + dxdy[i][0];
			newCol = col + dxdy[i][1];
				
			if (isMovable(newRow, newCol)) {
				visited[newRow][newCol] = 1;
				
				rq.push(newRow);
				cq.push(newCol);
				disq.push(dis + 1);
			}
		}
	}
	
	return 0;
}

int main(void) {
	string tmp;
	
	scanf("%d %d", &N, &M);
	
	for (int row = 1; row <= N; ++row) {
		cin >> tmp;
		
		for (int col = 1; col <= M; ++col) {
			maze[row][col] = tmp[col - 1] - 48;
		}
	}
	
	printf("%d", BFS());
	
	return 0;
}