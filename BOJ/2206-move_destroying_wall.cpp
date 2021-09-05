#include <stdio.h>
#include <string>
#include <iostream>
#include <queue>

using namespace std;

int N, M;
int map[1001][1001], t[1001][1001], wall[1001][1001];
int dxdy[4][2] = {
	{-1, 0},
	{0, 1},
	{1, 0},
	{0, -1}
};

int movable(int row, int col) {
	if (row > 0 && row <= N && col > 0 && col <= M) return 1;
	else return 0;
}

void BFS() {
	queue<int> rq, cq, wq;
	int tmpRow, tmpCol, tmpWall, newRow, newCol;
	
	rq.push(1);
	cq.push(1);
	wq.push(0);
	
	while (!rq.empty()) {
		tmpRow = rq.front();
		tmpCol = cq.front();
		tmpWall = wq.front();
		
		rq.pop();
		cq.pop();
		wq.pop();
		
		if (tmpRow == N && tmpCol == M) return;
		
		for (int i = 0; i < 4; ++i) {
			newRow = tmpRow + dxdy[i][0];
			newCol = tmpCol + dxdy[i][1];
			
			if (movable(newRow, newCol)) {
				if (map[newRow][newCol] == 0) {
					if (t[newRow][newCol] == 0 || (t[newRow][newCol] > 0 && tmpWall == 0 && wall[newRow][newCol] == 1)) {
						rq.push(newRow);
						cq.push(newCol);
						wq.push(tmpWall);
						wall[newRow][newCol] = tmpWall;
						t[newRow][newCol] = t[tmpRow][tmpCol] + 1;
					}
				} else {
					if (tmpWall == 0 && t[newRow][newCol] == 0) {
						rq.push(newRow);
						cq.push(newCol);
						wq.push(1);
						wall[newRow][newCol] = 1;
						t[newRow][newCol] = t[tmpRow][tmpCol] + 1;
					}
				}
			}
		}
	}
}

int main(void) {
	string tmp;
	
	scanf("%d %d", &N, &M);
	
	for (int row = 1; row <= N; ++row) {
		cin >> tmp;
		
		for (int col = 1; col <= M; ++col) {
			map[row][col] = tmp[col - 1] - '0';
		}
	}
	
	t[1][1] = 1;
	
	BFS();
	
	if (N == 1 && M == 1) {
		printf("1");
		
		return 0;
	}
	
	if (t[N][M] == 0) printf("-1");
	else printf("%d", t[N][M]);
	
	return 0;
}