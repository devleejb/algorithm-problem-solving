#include <stdio.h>
#include <vector>

using namespace std;

int N;
int isSelected[9];

void printPermutation(vector<int>& permutation) {
	if (permutation.size() == N) {
		for (int i = 0; i < N; ++i) {
			printf ("%d ", permutation[i]);	
		}
		
		printf("\n");
		
		return;
	}
	
	for (int i = 1; i <= N; ++i) {
		if (!isSelected[i]) {
			isSelected[i] = 1;
			permutation.push_back(i);
			
			printPermutation(permutation);
			
			isSelected[i] = 0;
			permutation.pop_back();
		}
	}
}

int main(void) {
	vector<int> permutation;
	
	// Input N
	scanf("%d", &N);
	
	printPermutation(permutation);
	
	return 0;
}