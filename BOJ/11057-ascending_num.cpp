#include <stdio.h>

using namespace std;

int N;
int num[1001][10];

void dp() {
	for (int digit = 2; digit <= N; ++digit) {
		for (int endNum = 0; endNum < 10; ++endNum) {
			for (int i = 0; i <= endNum; ++i) {
				num[digit][endNum] += num[digit - 1][i];
				num[digit][endNum] %= 10007;
			}
		}
	}
}

int main(void) {
	int sum = 0;
	
	scanf("%d", &N);
	
	num[1][0] = num[1][1] = num[1][2] = num[1][3] = num[1][4] = num[1][5] = num[1][6] = num[1][7] = num[1][8] = num[1][9] = 1; 

	dp();
	
	for (int i = 0; i < 10; ++i) {
		sum += num[N][i];
		sum %= 10007;
	}
	
	printf("%d", sum);
	
	return 0;
}