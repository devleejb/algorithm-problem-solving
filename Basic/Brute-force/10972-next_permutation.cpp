#include <stdio.h>
#include <algorithm>

using namespace std;

int N;
int permutation[10000];

void nextPermutation() {
	int idx = -1;
	
	for (int i = N - 1; i > 0; --i) {
		if (permutation[i] > permutation[i - 1]) {
			idx = i;
			
			break;
		}
	}
	
	if (idx == -1) {
		printf("-1");
		
		return;
	}
	
	for (int i = N - 1; i >= idx; --i) {
		if (permutation[idx - 1] < permutation[i]) {
			int tmp = permutation[i];
			permutation[i] = permutation[idx - 1];
			permutation[idx - 1] = tmp;
			
			break;
		}
	}
	
	sort(&permutation[idx], &permutation[idx] + (N - idx));
	
	for (int i = 0; i < N; ++i) {
		printf("%d ", permutation[i]);
	}
}

int main(void) {
	scanf("%d", &N);
	
	for (int i = 0; i < N; ++i) {
		scanf("%d", &permutation[i]);
	}
	
	nextPermutation();
	
	return 0;
}