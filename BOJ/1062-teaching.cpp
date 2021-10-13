#include <stdio.h>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

int N, K, cnt, alphaCnt;
int isLearned[27];
vector<string> words;

int checkWord(string& word) {
    for (int i = 0; i < word.size(); ++i) {
        if (isLearned[word[i] - 96] == 0) {
            return 0;
        }
    }

    return 1;
}

void checkAllWords() {
    int tmpCnt = 0;

    for (int i = 0; i < words.size(); ++i) {
        if (checkWord(words[i])) {
            ++tmpCnt;
        }
    }

    if (tmpCnt > cnt) cnt = tmpCnt;
}

void learnAplhabet(int previous) {
    if (alphaCnt == K) {
        checkAllWords();
        return;
    }

    if (previous < 26) {
        learnAplhabet(previous + 1);

        if (isLearned[previous + 1] == 0) {
            isLearned[previous + 1] = 1;
            ++alphaCnt;
            learnAplhabet(previous + 1);

            isLearned[previous + 1] = 0;
            --alphaCnt;
        }
    }
}

int main() {
    string tmpStr;

    scanf("%d %d", &N, &K);

    isLearned['a' - 96] = isLearned['n' - 96] = isLearned['t' - 96] = isLearned['i' - 96] = isLearned['c' - 96] = 1;
    
    alphaCnt = 5;

    for (int i = 0; i < N; ++i) {
        cin >> tmpStr;

        words.push_back(tmpStr);
    }

    learnAplhabet(0);

    printf("%d", cnt);

    return 0;
}