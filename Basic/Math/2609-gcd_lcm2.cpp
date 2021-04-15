#include <stdio.h>

using namespace std;

// Calculating gcd & lcm using Euclidean Algorithm

// Calculate GCD
int calculateGCD(int A, int B) {
	int r = A % B;
	
	while (r != 0) {
		A = B;
		B = r;
		r = A % B;
	}
	
	return B;
}

int main(void) {
	int A, B, gcd, lcm;
	
	scanf("%d %d", &A, &B);
	
	gcd = calculateGCD(A, B);
	lcm = A * B / gcd;
	
	printf("%d\n%d", gcd, lcm);
	
	return 0;
}