#include <stdio.h>
#include <vector>
#include <queue>

using namespace std;

int M, N, numOfRawTomato;
int garage[1000][1000];
int dxdy[4][2] = {
	{-1, 0},
	{0, 1},
	{1, 0},
	{0, -1}
};
queue<int> rq, cq, tq;

int isInIndex(int row, int col) {
	if (row >= 0 && row < N && col >= 0 && col < M) return 1;
	else return 0;
}

int BFS() {
	int tmpRow, tmpCol, tmpTime, newRow, newCol;
	
	while (!rq.empty()) {
		tmpRow = rq.front();
		tmpCol = cq.front();
		tmpTime = tq.front();
		
		rq.pop();
		cq.pop();
		tq.pop();
		
		for (int i = 0; i < 4; ++i) {
			newRow = tmpRow + dxdy[i][0];
			newCol = tmpCol + dxdy[i][1];
			
			if (isInIndex(newRow, newCol) && garage[newRow][newCol] == 0) {
				garage[newRow][newCol] = 1;
				rq.push(newRow);
				cq.push(newCol);
				tq.push(tmpTime + 1);
				
				if (--numOfRawTomato == 0) return tmpTime + 1;
			}
		}
	}
	
	if (numOfRawTomato == 0) return 0;
	else return -1;
}

int main(void) {
	int tmp;
	
	scanf("%d %d", &M, &N);
	
	for (int row = 0; row < N; ++row) {
		for (int col = 0; col < M; ++col) {
			scanf("%d", &tmp);
			
			garage[row][col] = tmp;
			
			if (tmp == 1) {
				rq.push(row);
				cq.push(col);
				tq.push(0);
			} else if (tmp == 0) {
				++numOfRawTomato;
			}
		}
	}
	
	printf("%d", BFS());
	
	return 0;
}