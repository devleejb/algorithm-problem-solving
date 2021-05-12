#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int N, M;
int num[8], isUsed[8];
vector<int> seq;

void printAllSequence() {
	if (seq.size() == M) {
		for (int i = 0; i < M; ++i) {
			printf("%d ", seq[i]);
		}
		
		printf("\n");
		
		return;
	}
	
	for (int i = 0; i < N; ++i) {
		if (isUsed[i] == 0) {
			isUsed[i] = 1;
			seq.push_back(num[i]);
			
			printAllSequence();
			
			isUsed[i] = 0;
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