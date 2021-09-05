#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> nine_dwarfs;

int findDwarfs(vector<int> dwarfs, int idx) {
	int ret;
	
	// Check already found 7 dwarfs
	if (dwarfs.size() == 7) {
		int sum = 0;
		
		for (int i = 0; i < 7; ++i) {
			sum += dwarfs[i];
		}
		
		if (sum == 100) {
			
			for (int i = 0; i < 7; ++i) printf("%d\n", dwarfs[i]);
			
			return 1;
		}
		
		return 0;
	}
	
	if (idx < 9) {
		dwarfs.push_back(nine_dwarfs[idx]);
		ret = findDwarfs(dwarfs, ++idx);

		if (ret == 1) return ret;

		dwarfs.pop_back();
		ret = findDwarfs(dwarfs, idx);

		if (ret == 1) return ret;
	}
	
	return 0;
}

int main(void) {
	int tmp;
	vector<int> vec;
	
	// Input 9 dwarfs
	for (int i = 0; i < 9; ++i) {
		scanf("%d", &tmp);
		
		nine_dwarfs.push_back(tmp);
	}
	
	// Sort 9 dwarfs
	sort(nine_dwarfs.begin(), nine_dwarfs.end());
	
	findDwarfs(vec, 0);
	
	return 0;
}