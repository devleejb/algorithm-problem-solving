#include <stdio.h>

using namespace std;

int N;
int T[15];
int P[15];
int maxVal = 0;

void maximizeValue(int day, int remainDays, int val) {
	if (day == N) {
		if (maxVal < val) maxVal = val;
	} else {
		++day;
		if (remainDays == 0 && T[day - 1] + day - 1 <= N) {
			maximizeValue(day, T[day - 1] - 1, val + P[day - 1]);
		}
		
		if (remainDays != 0) remainDays--;
		
		maximizeValue(day, remainDays, val);
	}
}

int main(void) {
	// Input N
	scanf("%d", &N);

	// Input T
	for (int i = 0; i < N; ++i) scanf("%d %d", &T[i], &P[i]);
	
	maximizeValue(0, 0, 0);
	
	printf("%d", maxVal);
	
	return 0;
}