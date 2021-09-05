#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, cnt;
int map[25][25];
int visited[25][25];
int dxdy[4][2] = {
	{-1, 0},
	{0, 1},
	{1, 0},
	{0, -1}
};

int isMovable(int row, int col) {
	if (row >= 0 && row < N && col >= 0 && col < N && visited[row][col] == 0 && map[row][col] == 1) return 1;
	else return 0;
}

void DFS(int row, int col) {
	int newRow, newCol;
	
	visited[row][col] = 1;
	
	for (int i = 0; i < 4; ++i) {
		newRow = row + dxdy[i][0];
		newCol = col + dxdy[i][1];
	
		if (isMovable(newRow, newCol)) {
			++cnt;
			DFS(newRow, newCol);
		}	
	}
}

int main(void) {
	string tmp;
	vector<int> ans;
	
	scanf("%d", &N);
	
	for (int row = 0; row < N; ++row) {
		cin >> tmp;
			
		for (int col = 0; col < N; ++col) {
			map[row][col] = tmp[col] - 48;
		}
	}
	
	for (int row = 0; row < N; ++row) {	
		for (int col = 0; col < N; ++col) {
			if (map[row][col] == 1 && visited[row][col] == 0) {
				cnt = 1;
				
				DFS(row, col);
				
				ans.push_back(cnt);
			}
		}
	}
	
	sort(ans.begin(), ans.end());
	
	printf("%d\n", (int) ans.size());
	
	for (int i = 0; i < ans.size(); ++i) {
		printf("%d\n", ans[i]);
	}
	
	return 0;
}