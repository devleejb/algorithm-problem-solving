#include <stdio.h>

using namespace std;

int N;
int P[1001];
int d[1001];

int dp(int n) {
	int minVal = 123456789;
	int val;
	
	if (n == 0) return 0;
	if (n == 1) return P[1];
	if (d[n] != 0) return d[n];
	
	for (int i = 1; i <= n; ++i) {
		val = P[i] + dp(n - i);
		
		if (val < minVal) minVal = val;
	}
	
	return d[n] = minVal;
}

int main(void) {
	scanf("%d", &N);
	
	for (int i = 1; i <= N; ++i) {
		scanf("%d", &P[i]);
	}
	
	printf("%d", dp(N));
	
	return 0;
}