#include <stdio.h>
#include <string>
#include <iostream>
#include <queue>

using namespace std;

int R, C, sRow, sCol, dRow, dCol;
char map[50][50];
int dis[50][50];
queue<int> rq, cq;
queue<char> tq;
int dxdy[4][2] = {
	{-1, 0},
	{0, 1},
	{1, 0},
	{0, -1}
};

int isMovable(int row, int col) {
	if (row >= 0 && row < R && col >= 0 && col < C) return 1;
	else return 0;
}

void BFS() {
	int tmpRow, tmpCol, newRow, newCol;
	char tmpType;
	
	rq.push(sRow);
	cq.push(sCol);
	tq.push('.');
	
	while (!rq.empty()) {
		tmpRow = rq.front();
		tmpCol = cq.front();
		tmpType = tq.front();
		
		rq.pop();
		cq.pop();
		tq.pop();
		
		for (int i = 0; i < 4; ++i) {
			newRow = tmpRow + dxdy[i][0];
			newCol = tmpCol + dxdy[i][1];
 			
			if (isMovable(newRow, newCol)) {
				if (tmpType == '.' && map[newRow][newCol] != 'X' && map[newRow][newCol] != '*' && map[newRow][newCol] != '-' && dis[newRow][newCol] == 0) {
					rq.push(newRow);
					cq.push(newCol);
					tq.push('.');
					
					dis[newRow][newCol] = dis[tmpRow][tmpCol] + 1;
				} else if (tmpType == '*' && map[newRow][newCol] != 'D' && map[newRow][newCol] != '*' && map[newRow][newCol] != '-' && map[newRow][newCol] != 'X') {
					map[tmpRow][tmpCol] = '*';
					map[newRow][newCol] = '-';
					
					rq.push(newRow);
					cq.push(newCol);
					tq.push('*');
				}
			}
		}
	}
}

int main(void) {
	string tmp;
	
	scanf("%d %d", &R, &C);
	
	for (int row = 0; row < R; ++row) {
		cin >> tmp;
		
		for (int col = 0; col < C; ++col) {
			if (tmp[col] == '.') {
				map[row][col] = '.';
			} else if (tmp[col] == '*') {
				map[row][col] = '*';
				rq.push(row);
				cq.push(col);
				tq.push('*');
			} else if (tmp[col] == 'X') {
				map[row][col] = 'X';
			} else if (tmp[col] == 'S') {
				map[row][col] = '.';
				
				sRow = row;
				sCol = col;
			} else if (tmp[col] == 'D') {
				map[row][col] = 'D';
				
				dRow = row;
				dCol = col;
			}
		}
	}
	
	BFS();
	
	if (dis[dRow][dCol] == 0) printf("KAKTUS");
	else printf("%d", dis[dRow][dCol]);
	
	return 0;
}