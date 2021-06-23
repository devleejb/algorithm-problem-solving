#include <stdio.h>

using namespace std;

int N;
int num[1001];

int main() {
	scanf("%d", &N);
	
	num[1] = 1;
	num[2] = 3;
	
	for (int i = 3; i <= N; ++i) {
		num[i] = (num[i - 1] + num[i - 2] * 2) % 10007;
	}
	
	printf("%d", num[N]);
	
	return 0;
}