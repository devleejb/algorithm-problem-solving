#include <stdio.h>

using namespace std;

long long N, S;
long long series[20];
long long ans;

void countSubSeriesSum(int idx, int sum, int isIncreased) {
	if (isIncreased == 1 && sum == S) ans++;
	
	if (idx < N) {
		countSubSeriesSum(++idx, sum, 0);
		countSubSeriesSum(idx, sum + series[idx - 1], 1);
	}
}

int main(void) {
	// Input N & S
	scanf("%lld %lld", &N, &S);

	// Input Series
	for (int i = 0; i < N; ++i) {
		scanf("%lld", &series[i]);
	}
	
	countSubSeriesSum(0, 0, 0);
	
	printf("%lld", ans);
	
	return 0;
}