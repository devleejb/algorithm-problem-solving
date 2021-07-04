#include <stdio.h>

using namespace std;

int T, N, maxVal;
int board[2][100000];
int d[2][100000];

void dp() {
	for (int col = 2; col < N; ++col) {
		for (int row = 0; row < 2; ++row) {
			d[row][col] = (d[!row][col - 1] > d[!row][col - 2] ? d[!row][col - 1] : d[!row][col - 2]) + board[row][col];	
		} 
	}
}

int main() {
	scanf("%d", &T);
	
	for (int i = 0; i < T; ++i) {
		scanf("%d", &N);
		
		for (int row = 0; row < 2; ++row) {
			for (int col = 0; col < N; ++col) {
				scanf("%d", &board[row][col]);
			}
		}
		
		d[0][0] = board[0][0];
		d[1][0] = board[1][0];
		d[0][1] = d[1][0] + board[0][1];
		d[1][1] = d[0][0] + board[1][1];
		
		dp();
		
		maxVal = d[0][N - 1] > d[1][N - 1] ? d[0][N - 1] : d[1][N - 1];
	
		printf("%d\n", maxVal);
	}
	
	return 0;
}