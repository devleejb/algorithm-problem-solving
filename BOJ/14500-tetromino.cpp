#include <stdio.h>

using namespace std;

int N, M;
int paper[500][500];
int tetromino[19][3][2] = {{{1, 0}, {2, 0}, {3, 0}}, 
						   {{0, 1}, {0, 2}, {0, 3}}, 
						   {{1, 0}, {1, 1}, {0, 1}}, 
						   {{0, 1}, {1, 1}, {1, 2}}, 
						   {{1, 0}, {1, -1}, {2, -1}}, 
						   {{1, 0}, {2, 0}, {1, 1}},
						   {{1, 0}, {1, -1}, {1, 1}},
						   {{0, 1}, {-1, 1}, {1, 1}},
						   {{0, 1}, {1, 1}, {0, 2}},
						   {{0, 1}, {0, 2}, {1, 2}},
						   {{1, 0}, {0, 1}, {2, 0}},
						   {{1, 0}, {1, 1}, {1, 2}},
						   {{1, 0}, {2, 0}, {2, -1}},
						   {{0, 1}, {-1, 1}, {-1, 2}},
						   {{1, 0}, {1, 1}, {2, 1}},
						   {{1, 0}, {1, -1}, {1, -2}},
						   {{0, 1}, {1, 1}, {2, 1}},
						   {{-1, 0}, {-1, 1}, {-1, 2}},
						   {{1, 0}, {2, 0}, {2, 1}}
						  };

int isInRange(int i, int j, int k) {
	for (int c = 0; c < 3; ++c) {
		if (!(i + tetromino[k][c][1] >= 0 && i + tetromino[k][c][1] < N && j + tetromino[k][c][0] >= 0 && j + tetromino[k][c][0] < M)) return 0;
	}
	
	return 1;
}

int makeSum(int i, int j, int k) {
	int sum = paper[i][j];
	
	for (int c = 0; c < 3; ++c) {
		sum += paper[i + tetromino[k][c][1]][j + tetromino[k][c][0]];	
	}
	
	return sum;
}

int maxTetromino() {
	int max = 0;
	int tmp = 0;
	
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			for (int k = 0; k < 19; ++k) {
				if (isInRange(i, j, k)) {
					tmp = makeSum(i, j, k);
					
					if (tmp > max) {
						max = tmp;
					}
				}
			}	
		}
	}
	
	return max;
}

int main(void) {
	// Input N, M
	scanf("%d %d", &N, &M);
	
	// Input paper
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			scanf("%d", &paper[i][j]);
		}
	}
	
	// Calculate and Print result
	printf("%d", maxTetromino());
	
	return 0;
}