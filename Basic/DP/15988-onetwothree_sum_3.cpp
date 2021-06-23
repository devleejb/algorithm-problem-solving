#include <stdio.h>
#include <vector>

using namespace std;

int T;
long long num[1000001];
vector<int> N;

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
	
	for (int i = 4; i <= 1000000; ++i) {
		num[i] = (num[i - 1] + num[i - 2] + num[i - 3]) % 1000000009;
	}
	
	for (int i = 0; i < T; ++i) {
		printf("%lld\n", num[N[i]]);
	}
	
	return 0;
}