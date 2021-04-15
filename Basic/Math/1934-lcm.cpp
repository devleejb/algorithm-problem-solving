#include <stdio.h>

using namespace std;

int results[1000];

// Calculate GCD using Euclidean Algorithm
int calcuateGCD(int A, int B) {
	int r = A % B;
	
	while (r != 0) {
		A = B;
		B = r;
		r = A % B;
	}
	
	return B;
}

int main(void) {
	int T, A, B;
	
	// Input T
	scanf("%d", &T);
	
	// Input A, B and calcualte lcm
	for (int i = 0; i < T; ++i) {
		scanf("%d %d", &A, &B);
		
		results[i] = A * B / calcuateGCD(A, B);
	}
	
	// Print results
	for (int i = 0; i < T; ++i) {
		printf("%d\n", results[i]);
	}
	
	return 0;
}