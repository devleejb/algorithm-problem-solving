#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int L, C;
vector<char> s;

void makePW(int nowChar, vector<char>& pw) {
	if (pw.size() == L) {
		int vowel = 0; // 모음
		int consonant = 0; // 자음
		
		for (int i = 0; i < L; ++i) {
			if (pw[i] == 'a' || pw[i] == 'e' || pw[i] == 'i' || pw[i] == 'o' || pw[i] == 'u') vowel++;
		}
		
		consonant = L - vowel;
		
		if (!(vowel >= 1 && consonant >= 2)) return;
		
		for (int i = 0; i < L; ++i) printf("%c", pw[i]);
		
		printf("\n");
	} else if (nowChar < C) {
		pw.push_back(s[nowChar++]);
		makePW(nowChar, pw);
		
		pw.pop_back();
		makePW(nowChar, pw);
	}
} 

int main(void) {
	vector<char> pw;
	char tmp;
	
	// Input L & C
	scanf("%d %d\n", &L, &C);

	// Input Character set
	for (int i = 0; i < C; ++i) {
		scanf("%c", &tmp);
		s.push_back(tmp);
		
		scanf("%c", &tmp);
	}
	
	sort(s.begin(), s.end());
	
	makePW(0, pw);
	
	return 0;
}