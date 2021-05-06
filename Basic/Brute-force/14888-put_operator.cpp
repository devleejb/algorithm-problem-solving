#include <stdio.h>

using namespace std;

int N;
int seq[11];
int numOfOperator[4];
int maxVal = -1234567890;
int minVal = 1234567890;

void putOperator(int pos, int val) {
	if (pos == N - 1) {
		if (maxVal < val) {
			maxVal = val;
		}
		if (minVal > val) {
			minVal = val;
		}
	}
	
	pos++;
	
	for (int i = 0; i < 4; ++i) {
		if (numOfOperator[i] > 0) {
			numOfOperator[i]--;
			
			switch(i) {
				case 0:
					putOperator(pos, val + seq[pos]);
					break;
				case 1:
					putOperator(pos, val - seq[pos]);
					break;
				case 2:	
					putOperator(pos, val * seq[pos]);
					break;
				case 3: 
					putOperator(pos, val / seq[pos]);
					break;
			}
			
			numOfOperator[i]++;
		}
	}
}

int main(void) {
	// Input N
	scanf("%d", &N);

	// Input sequence
	for (int i = 0; i < N; ++i) {
		scanf("%d", &seq[i]);
	}
	
	// Input num of operator
	for (int i = 0; i < 4; ++i) {
		scanf("%d", &numOfOperator[i]);
	}
	
	putOperator(0, seq[0]);
	
	printf("%d\n%d", maxVal, minVal);
	
	return 0;
}