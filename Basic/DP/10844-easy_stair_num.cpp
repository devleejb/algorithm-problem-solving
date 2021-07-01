#include <stdio.h>

using namespace std;

int N;
int d[101][10];

void dp() {
	for (int digit = 2; digit <= N; ++digit) {
		for (int endNum = 0; endNum <= 9; ++endNum) {
			if (endNum - 1 >= 0) {
				d[digit][endNum] += d[digit - 1][endNum - 1];
				
				d[digit][endNum] %= 1000000000;
			}
			
			if (endNum + 1 <= 9) {
				d[digit][endNum] += d[digit - 1][endNum + 1];
			
				d[digit][endNum] %= 1000000000;
			}
		}
	}

}

int main(void) {
	int sum = 0;
	
	scanf("%d", &N);
	
	d[1][1] = d[1][2] = d[1][3] = d[1][4] = d[1][5] = d[1][6] = d[1][7] = d[1][8] = d[1][9] = 1;
	
	dp();
	
	for (int i = 0; i <= 9; ++i) {
		sum += d[N][i];
		
		sum %= 1000000000;
	}
	
	printf("%d", sum);
	
	return 0;
}