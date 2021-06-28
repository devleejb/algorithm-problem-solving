#include <stdio.h>
#include <vector>

using namespace std;

int T, maxInput;
int d[100001][4];
vector<int> input;

void dp() {
	for (int n = 3; n <= maxInput; ++n) {
		for (int endNum = 1; endNum < 4; ++endNum) {
			for (int i = 1; i <= 3; ++i) {
				if (i != endNum && n - endNum > 0) {
					d[n][endNum] += d[n - endNum][i];
					d[n][endNum] %= 1000000009;
				}
			}
		}
	}
}

int main(void) {
	int tmp, sum;
	
	scanf("%d", &T);
	
	for (int i = 0; i < T; ++i) {
		scanf("%d", &tmp);
		
		input.push_back(tmp);
	
		if (tmp > maxInput) maxInput = tmp;
	}
	
	d[1][1] = 1;
	d[2][2] = 1;
	d[3][3] = 1;
	
	dp();
	
	for (int i = 0; i < T; ++i) {
		sum = 0;
		tmp = input[i];
		
		for (int j = 1; j <= 3; ++j) {
			sum += d[tmp][j];
			sum %= 1000000009;
		}
		
		printf("%d\n", sum);
	}
	
	return 0;
}