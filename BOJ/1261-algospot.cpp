#include <stdio.h>
#include <queue>
#include <string>
#include <iostream>

using namespace std;

int M, N;
int maze[100][100];
int wall[100][100];
int dxdy[4][2] = {
	{-1, 0},
	{0, 1},
	{1, 0},
	{0, -1}
};
queue<int> rq, cq;

int isInIndex(int row, int col) {
	if (row >= 0 && row < N && col >= 0 && col < M) return 1;
	else return 0;
}

void BFS() {
	int tmpRow, tmpCol, newRow, newCol;
	
	wall[0][0] = 0;
	
	rq.push(0);
	cq.push(0);
	
	while (!rq.empty()) {
		tmpRow = rq.front();
		tmpCol = cq.front();
		rq.pop();
		cq.pop();
		
		for (int i = 0; i < 4; ++i) {
			newRow = tmpRow + dxdy[i][0];
			newCol = tmpCol + dxdy[i][1];
		
			if (isInIndex(newRow, newCol) && (wall[newRow][newCol] == -1 || wall[newRow][newCol] > wall[tmpRow][tmpCol] + maze[newRow][newCol])) {
				wall[newRow][newCol] = wall[tmpRow][tmpCol] + maze[newRow][newCol];
				
				rq.push(newRow);
				cq.push(newCol);
			}
		}
	}
}

int main(void) {
	string tmp;
	
	scanf("%d %d", &M, &N);
	
	for (int row = 0; row < N; ++row) {
		cin >> tmp;
		
		for (int col = 0; col < M; ++col) {
			maze[row][col] = tmp[col] - 48;	
			wall[row][col] = -1;
		}
	}
	
	BFS();
	
	printf("%d", wall[N - 1][M - 1]);
	
	return 0;
}