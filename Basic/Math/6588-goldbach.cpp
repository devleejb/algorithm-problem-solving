#include <stdio.h>
#include <math.h>

using namespace std;

int arr[1000001];
int c[100000];

void isConjectureTrue(int num) {
	for (int i = 2; i <= num / 2; ++i) {
		if (arr[i] == 0 && arr[num - i] == 0) {
			printf("%d = %d + %d\n", num, i, num - i);
			
			return;
		}
	}
	
	printf("Goldbach's conjecture is wrong.\n");
}

void makePrimeNumber(int maxNum) {
	int end = sqrt(maxNum);
	
	for (int i = 2; i <= end; ++i){
		if (arr[i] == 1) continue;
		
		for (int j = 2; i * j <= maxNum; ++j) {
			arr[i * j] = 1;
		}
	}
}

int main(void) {
	int maxNum = 0;
	int tmp = -1;
	int idx = 0;
	
	while (tmp != 0) {
		scanf("%d", &tmp);
		
		c[idx++] = tmp;
		
		if (tmp > maxNum) maxNum = tmp;
	}
	
	--idx;
	
	makePrimeNumber(maxNum);
	
	for (int i = 0; i < idx; ++i) {
		isConjectureTrue(c[i]);
	}
	
	
	return 0;
}