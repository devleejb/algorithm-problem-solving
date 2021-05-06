#include <stdio.h>
#include <vector>

using namespace std;

int T;
int results[11];

// Calculate One Two Three sum in (0, 11)
void onetwothreesum(int currentSum) {
	int sum = 0;
	
	for (int i = 1; i <= 3; ++i) {
		sum = currentSum + i;
		
		if (sum < 11) {
			++results[sum];
			onetwothreesum(sum);
		}
	}
}

int main(void) {
	vector<int> input;
	int tmp;
	
	// Input T
	scanf("%d", &T);
	
	// Input integers
	for (int i = 0; i < T; ++i) {
		scanf("%d", &tmp);
		
		input.push_back(tmp);
	}
	
	onetwothreesum(0);
	
	// Print results
	for (int i = 0; i < T; ++i) {
		printf("%d\n", results[input[i]]);
	}
	
	return 0;
}