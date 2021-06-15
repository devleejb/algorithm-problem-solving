#include <stdio.h>

using namespace std;

int arr[1000001];
int N;

void DP() {
	for (int i = 1; i <= N; ++i) {
		if (i * 3 <= N && (arr[i * 3] > arr[i] + 1|| arr[i * 3] == 0)) arr[i * 3] = arr[i] + 1;
		if (i * 2 <= N && (arr[i * 2] > arr[i] + 1|| arr[i * 2] == 0)) arr[i * 2] = arr[i] + 1;
		if (i + 1 <= N && (arr[i + 1] > arr[i] + 1|| arr[i + 1] == 0)) arr[i + 1] = arr[i] + 1;
	}
}

int main(void) {
	scanf("%d", &N);
	
	DP();
	
	printf("%d", arr[N]);
	
	return 0;
}