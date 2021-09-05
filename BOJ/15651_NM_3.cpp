#include <stdio.h>
#include <vector>

using namespace std;

int N, M;
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
			seq.push_back(i);
			
			printAllSequence();
			
			seq.pop_back();
	}
}

int main(void) {
	scanf("%d %d", &N, &M);
	
	printAllSequence();
	
	return 0;
}