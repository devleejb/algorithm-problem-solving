#include <stdio.h>

using namespace std;

int w, h;
int map[50][50];
int move[8][2] = {
	{-1, -1},
	{-1, 0},
	{-1, 1},
	{0, 1},
	{1, 1},
	{1, 0},
	{1, -1},
	{0, -1}
};

int isInGraph(int row, int col) {
	if (row >= 0 && row < h && col >= 0 && col < w) return 1;
	else return 0;
}

void DFS(int verRow, int verCol, int visited[50][50]) {
	int row, col;
	
	visited[verRow][verCol] = 1;
	
	for (int i = 0; i < 8; ++i) {
		row = verRow + move[i][0];
		col = verCol + move[i][1];
		
		if(isInGraph(row, col) && map[row][col] == 1 && visited[row][col] == 0) {
			DFS(row, col, visited);
		}
	}
}

int main(void) {
	int cnt = 0;
	
	scanf("%d %d", &w, &h);
	
	while (!(w == 0 && h == 0)) {
		int visited[50][50] = {0};
		
		cnt = 0;
		
		for (int row = 0; row < h; ++row) {
			for (int col = 0; col < w; ++col) {
				scanf("%d", &map[row][col]);
			}
		}
		
		for (int row = 0; row < h; ++row) {
			for (int col = 0; col < w; ++col) {
				if (map[row][col] == 1 && visited[row][col] == 0) {
					++cnt;
					DFS(row, col, visited);
				}
			}
		}
		
		printf("%d\n", cnt);
		
		scanf("%d %d", &w, &h);
	}
	
	return 0;
}