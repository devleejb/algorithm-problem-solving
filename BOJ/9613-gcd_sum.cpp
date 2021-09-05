#include <stdio.h>

using namespace std;

long long results[100];
int num[100];

// Calculate GCD
long long calculateGCD(int A, int B) {
	int r;
	
	// Case : A < B
	if (A < B) {
		int tmp = A;
		
		A = B;
		B = tmp;
	}
	
	r = A % B;
	
	while (r != 0) {
		A = B;
		B = r;
		r = A % B;
	}
	
	return B;
}

int main(void) {
	int T, n;
	long long gcdSum;
	
	// Input T
	scanf("%d", &T);
	
	// Input n, numbers and Cacluate GCD sum
	for (int t = 0; t < T; ++t) {
		gcdSum = 0;
		
		scanf("%d", &n);
		
		for (int i = 0; i < n; ++i) {
			scanf("%d", &num[i]);
		}
		
		for (int i = 0; i < n - 1; ++i) {
			for (int j = i + 1; j < n; ++j) {
				gcdSum += calculateGCD(num[i], num[j]);
			}
		}
		
		results[t] = gcdSum;
	}
	
	// Print results
	for (int t = 0; t < T; ++t) {
		printf("%lld\n", results[t]);
	}
	
	return 0;
}