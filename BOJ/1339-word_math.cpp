#include <stdio.h>
#include <vector>
#include <string>
#include <iostream>
#include <stdlib.h>
#include <cmath>

using namespace std;

int N, alphabetSize, idx, maxVal;
int alphabet[26], weight[10], isUsed[10];
string tmp;
vector<int> score;

void calMax() {
    if (score.size() == alphabetSize) {
        int sum = 0;
        
        for (int i = 0; i < alphabetSize; ++i) {
            sum += score[i] * weight[i];
        }

        if (sum > maxVal) maxVal = sum;
    } else {
        for (int i = 0; i < 10; ++i) {
            if (isUsed[i] == 0) {
                isUsed[i] = 1;
                score.push_back(i);

                calMax();

                isUsed[i] = 0;
                score.pop_back();
            }
        }
    }
}

int main() {
    scanf("%d", &N);

    for (int i = 0; i < N; ++i) {
        cin >> tmp;

        for (int j = 0; j < tmp.size(); ++j) {
            if (alphabet[tmp[j] - 'A'] == 0) {
                alphabet[tmp[j] - 'A'] = --idx;
                ++alphabetSize;      
            }

            weight[abs(alphabet[tmp[j] - 'A']) - 1] += pow(10, tmp.size() - j - 1);
        }
    }

    alphabetSize = abs(idx);

    calMax();

    printf("%d", maxVal);

    return 0;
}