#include <stdio.h>
#include <vector>

using namespace std;

int T;
int num[11];
vector<int> N;

int dp(int n) {
	if (num[n] != 0) return num[n];
	
	return num[n] = dp(n - 1) + dp(n - 2) + dp(n - 3);
}

int main() {
	int tmp;
	
	scanf("%d", &T);
	
	for (int i = 0; i < T; ++i) {
		scanf("%d", &tmp);
		
		N.push_back(tmp);
	}
	
	num[1] = 1;
	num[2] = 2;
	num[3] = 4;
	
	dp(10);
	
	
	for (int i = 0; i < T; ++i) {
		printf("%d\n", num[N[i]]);
	}
	
	return 0;
}