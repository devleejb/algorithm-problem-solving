#include <stdio.h>

using namespace std;

int N;
long long d[91][2];

void dp() {
	for (int n = 2; n <= N; ++n) {
		d[n][1] = d[n - 1][0];
		d[n][0] = d[n - 1][0] + d[n - 1][1];
	}
}

int main(void) {
	scanf("%d", &N);
	
	d[1][0] = 0;
	d[1][1] = 1;
	
	dp();
	
	printf("%lld", d[N][0] + d[N][1]);
	
	return 0;
}