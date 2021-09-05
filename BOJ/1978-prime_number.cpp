#include <stdio.h>

using namespace std;

// Return 1 if n is a prime number
int isPrimeNumber(int n) {
	if (n == 1) return 0; 
		
	for (int i = 2; i <= n / 2; ++i) {
		if (n % i == 0) {
			return 0;
		}
	}
	
	return 1;
}

int main(void) {
	int N, n, result = 0;
	
	// Input N
	scanf("%d", &N);
	
	// Input N numbers
	for (int i = 0; i < N; ++i) {
		scanf("%d", &n);
		
		result += isPrimeNumber(n);
	}
	
	// Print result
	printf("%d", result);
	
	return 0;
}