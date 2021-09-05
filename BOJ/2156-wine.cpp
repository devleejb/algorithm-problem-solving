#include <stdio.h>

using namespace std;

int N, maxVal;
int wine[10001], maxWine[10001][3];

int calAmountOfWine() {
    maxWine[1][1] = maxVal = wine[1];
	
	for (int n = 2; n <= N; ++n) {
        maxWine[n][0] = maxVal;
		maxWine[n][1] = maxWine[n - 1][0] + wine[n];
		maxWine[n][2] = maxWine[n - 1][1] + wine[n];
		
		maxVal = maxWine[n][0] > maxWine[n][1] ? maxWine[n][0] : maxWine[n][1];
		maxVal = maxVal > maxWine[n][2] ? maxVal : maxWine[n][2];
    }
	
	
	return maxVal;
}

int main() {
    scanf("%d", &N);
	
	for (int n = 1; n <= N; ++n) {
        scanf("%d", &wine[n]);
    }
	
	printf("%d", calAmountOfWine());
	
    return 0;
}