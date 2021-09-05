#include <stdio.h>
#include <vector>

using namespace std;

void makeLottoNumber(vector<vector<int>>& result, vector<int>& s, vector<int>& selected, int nowNum) {
	if (selected.size() == 6) {
		result.push_back(selected);
	} else if (nowNum < s.size()) {
		selected.push_back(s[nowNum]);
		makeLottoNumber(result, s, selected, nowNum + 1);
		
		selected.pop_back();
		makeLottoNumber(result, s, selected, nowNum + 1);
	}
}

void printResult(vector<vector<int>> result) {
	for (int i = 0; i < result.size(); ++i) {
		for (int j = 0; j < result[i].size(); ++j) {
			printf("%d ", result[i][j]);
		}
		
		printf("\n");
	}
}

int main(void) {
	vector<vector<int>> set;
	int k, tmp, idx = -1;
	
	scanf("%d", &k);
	
	while (k != 0) {
		vector<int> s;
		
		set.push_back(s);
		++idx;
		
		for (int i = 0; i < k; ++i) {
			scanf("%d", &tmp);
			
			set[idx].push_back(tmp);
		}
		
		scanf("%d", &k);
	}
	
	for (int i = 0; i < set.size(); ++i) {
		vector<vector<int>> result;
		vector<int> selected;
		
		makeLottoNumber(result, set[i], selected, 0);
		
		printResult(result);
		
		if (i != set.size() - 1) {
			printf("\n");
		}
	}
	
	return 0;
} 