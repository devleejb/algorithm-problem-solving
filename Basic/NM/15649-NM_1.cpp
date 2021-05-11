#include <stdio.h>
#include <vector>

using namespace std;

int N, M;
int isUsed[9];
vector<int> seq;

void printAllSequence() {
	if (seq.size() == M) {
		for (int i = 0; i < M; ++i) {
			printf("%d ", seq[i]);
		}
		
		printf("\n");
		
		return;
	}
	
	for (int i = 1; i <= N; ++i) {
		if (isUsed[i] == 0) {
			seq.push_back(i);
			isUsed[i] = 1;
			
			printAllSequence();
			
			seq.pop_back();
			isUsed[i] = 0;
		}
	}
}

int main(void) {
	scanf("%d %d", &N, &M);
	
	printAllSequence();
	
	return 0;
}