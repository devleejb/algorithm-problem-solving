#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

int N, maxVal;
int arr[8];
int isSelected[8];

void maximizeDifference(vector<int>& vec) {
	if (vec.size() == N) {
		int sum = 0;
		
		for (int i = 1; i < N; ++i) {
			sum += abs(vec[i - 1] - vec[i]);
		}
		
		if (maxVal < sum) maxVal = sum;
		
		return;
	}
	
	for (int i = 0; i < N; ++i) {
		if (isSelected[i] == 0) {
			vec.push_back(arr[i]);
			isSelected[i] = 1;
			
			maximizeDifference(vec);
			
			vec.pop_back();
			isSelected[i] = 0;
		}
	}
}

int main(void) {
	vector<int> vec;
	
	// Input N
	scanf("%d", &N);

	// Input integer
	for (int i = 0; i < N; ++i) {
		scanf("%d", &arr[i]);
	}
	
	maximizeDifference(vec);
	
	printf("%d", maxVal);
	
	return 0;
}