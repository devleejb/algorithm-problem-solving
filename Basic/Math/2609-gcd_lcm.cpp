#include <stdio.h>

using namespace std;

// Calculate gcd
int calculateGCD(int A, int B) {
	int min = A > B ? B : A;
	int gcd = 1;
	
	for (int i = 2; i <= min; ++i) {
		if (A % i == 0 && B % i == 0) {
			gcd = i;
		}
	}
	
	return gcd;
}

// Calculate lcm
int calculateLCM(int A, int B) {
	int min = A > B ? B : A, AVal = A, BVal = B;
	
	while (AVal != BVal) {
		if (AVal < BVal) AVal += A;
		else BVal += B;
	}
	
	return AVal;
}

int main(void) {
	int A, B, gcd, lcm;
	
	// Input A, B
	scanf("%d %d", &A, &B);
	
	// Calculate gcd & lcm
	gcd = calculateGCD(A, B);
	lcm = calculateLCM(A, B);
	
	// Print gcd, lsm
	printf("%d\n%d", gcd, lcm);
	
	return 0;
	
}