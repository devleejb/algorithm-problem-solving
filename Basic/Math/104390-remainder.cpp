#include <stdio.h>

using namespace std;

int main(void) {
	int A, B, C, result1, result2;
	
	// Input A, B, C
	scanf("%d %d %d", &A, &B, &C);
	
	// Calculate expression
	result1 = (A + B) % C;
	result2 = (A * B) % C;
	
	// Print result
	printf("%d\n%d\n%d\n%d", result1, result1, result2, result2);

	return 0;
}