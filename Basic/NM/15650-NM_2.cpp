#include <stdio.h>
#include <vector>

using namespace std;

int N, M;
int isUsed[9];
vector<int> seq;

void printAllSequence(int nextNum) {
	if (seq.size() == M) {
		for (int i = 0; i < M; ++i) {
			printf("%d ", seq[i]);
		}
		
		printf("\n");
		
		return;
	}
	
	for (int i = nextNum; i <= N; ++i) {
		if (isUsed[i] == 0) {
			seq.push_back(i);
			isUsed[i] = 1;
			
			printAllSequence(i + 1);
			
			seq.pop_back();
			isUsed[i] = 0;
		}
	}
}

int main(void) {
	scanf("%d %d", &N, &M);
	
	printAllSequence(1);
	
	return 0;
}