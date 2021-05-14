#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int N, M;
int num[8];
vector<int> seq;

void printAllSequence() {
	int isUsedThisTurn[10000] = { 0 };
	
	if (seq.size() == M) {
		for (int i = 0; i < M; ++i) {
			printf("%d ", seq[i]);
		}
		
		printf("\n");
		
		return;
	}
	
	for (int i = 0; i < N; ++i) {
		if (isUsedThisTurn[num[i]] == 0) {
			isUsedThisTurn[num[i]] = 1;
			seq.push_back(num[i]);
			
			printAllSequence();
			
			seq.pop_back();
		}
	}
}

int main(void) {
	scanf("%d %d", &N, &M);
	
	for (int i = 0; i < N; ++i) {
		scanf("%d", &num[i]);
	}
	
	sort(num, num + N);

	printAllSequence();
	
	return 0;
}