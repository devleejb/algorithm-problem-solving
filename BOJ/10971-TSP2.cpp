#include <stdio.h>
#include <vector>

using namespace std;

int N, minVal = 1234567890;
int cost[10][10];
int isVisited[10];

void TSP2(vector<int>& vec, int nowCity) {
	if (vec.size() == N - 1) {
		int sum = cost[0][vec[0]];
	
		
		for (int i = 0; i < N - 2; ++i) {
			sum += cost[vec[i]][vec[i + 1]];
		}
		
		if (cost[vec[N - 2]][0] == 0) return;
		
		sum += cost[vec[N - 2]][0];
		
		if (minVal > sum) minVal = sum;
		
		return;
	}
	
	for (int i = 1; i < N; ++i) {
		if (isVisited[i] == 0 && cost[nowCity][i] != 0) {
			vec.push_back(i);
			isVisited[i] = 1;
			
			TSP2(vec, i);
			
			vec.pop_back();
			isVisited[i] = 0;
		}
	}
}

int main(void) {
	vector<int> vec;
	
	// Input N
	scanf("%d", &N);
	
	// Input Adjacency Matrix
	for (int row = 0; row < N; ++row) {
		for (int col = 0; col < N; ++col) {
			scanf("%d", &cost[row][col]);
		}
	}
	
	// start point
	isVisited[0] = 1;
	
	TSP2(vec, 0);
	
	printf("%d", minVal);
	
	return 0;
}