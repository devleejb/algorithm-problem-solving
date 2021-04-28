#include <stdio.h>

using namespace std;

int E, S, M, e, s, m;

int calculateDate() {
	int year = 0;
	
	while (!(E == e && S == s && M == m)) {
		++year;

		e = ++e % 16;
		s = ++s % 29;
		m = ++m % 20;
		
		if (e == 0) ++e;
		if (s == 0) ++s;
		if (m == 0) ++m;
	}
	
	return year;
}

int main(void) {
	// Input E, S, M
	scanf("%d %d %d", &E, &S, &M);
	
	// Print year
	printf("%d", calculateDate());
	
	return 0;
}