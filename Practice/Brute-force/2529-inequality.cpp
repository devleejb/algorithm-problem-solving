#include <stdio.h>
#include <vector>
#include <cmath>
#include <string>
#include <iostream>

using namespace std;

int K, inequality[10], isUsed[10];
long long minVal = 9876543210, maxVal;
vector<int> selected;
string minStr, maxStr;

void calMinMax(vector<int>& selected) {
    if (selected.size() == K + 1) {
        long long num = 0;
        string numStr = "";

        for (int i = K; i >= 0; --i) {
            num += selected[K - i] * pow(10, i);
            numStr += to_string(selected[K - i]);
        }

        if (num < minVal) {
            minStr = numStr;
            minVal = num;
        }
        else if (num > maxVal) {
            maxStr = numStr;
            maxVal = num;
        }

        return;
    }

    for (int i = 0; i < 10; ++i) {
        if (selected.size() == 0) {
            selected.push_back(i);
            isUsed[i] = 1;

            calMinMax(selected);

            selected.pop_back();
            isUsed[i] = 0;
        } else {
            // > : 0 / < : 1
            if (isUsed[i] == 0) {
                if (inequality[selected.size() - 1] == 0) {
                    if (selected[selected.size() - 1] > i) {
                        selected.push_back(i);
                        isUsed[i] = 1;

                        calMinMax(selected);

                        selected.pop_back();
                        isUsed[i] = 0;
                    }
                } else {
                    if (selected[selected.size() - 1] < i) {
                        selected.push_back(i);
                        isUsed[i] = 1;

                        calMinMax(selected);

                        selected.pop_back();
                        isUsed[i] = 0;
                    }
                }
            }
        }
    }
}

int main() {
    char tmp;

    scanf("%d", &K);

    for (int i = 0; i < K; ++i) {
        scanf(" %c", &tmp);

        if (tmp == '<') {
            inequality[i] = 1;
        }
    }

    calMinMax(selected);

    printf("%s\n%s", maxStr.c_str(), minStr.c_str());

    return 0;
}