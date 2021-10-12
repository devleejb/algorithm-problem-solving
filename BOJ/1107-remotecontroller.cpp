#include <stdio.h>
#include <vector>
#include <string>

using namespace std;

vector<int> number;
int rc[10];
int smallerMax = -123456789, biggerMin = 123456789, N, M, digit, smallerMaxDigit, biggerMinDigit;

int makeNumber() {
    int num = 0;

    for (int i = 0; i < number.size(); ++i) {
        num *= 10;
        num += number[i];
    }

    return num;
}

void permutation() {
    string tmp;
    if (number.size() != 0) {
        int num = makeNumber();

        if (num <= N && num > smallerMax) {
            smallerMax = num;
            tmp = to_string(num);
            smallerMaxDigit = tmp.size();
        } else if (num > N && num < biggerMin) {
            biggerMin = num;
            tmp = to_string(num);
            biggerMinDigit = tmp.size();
        }
    }

    if (number.size() <= digit) {
        for (int i = 0; i < 10; ++i) {
            if (rc[i] == 0) {
                number.push_back(i);
                permutation();
                number.pop_back();
            }
        }
    }
}

int main() {
    int tmp, onlyButton, fromBigger, fromSmaller;
    string tmpStr;

    scanf("%d %d", &N, &M);

    tmpStr = to_string(N);
    digit = tmpStr.size();

    for (int i = 0; i < M; ++i) {
        scanf("%d", &tmp);
        rc[tmp] = 1;
    }

    permutation();

    onlyButton = abs(100 - N);
    fromBigger = biggerMin - N + biggerMinDigit;
    fromSmaller = N - smallerMax + smallerMaxDigit;

    if (onlyButton <= fromBigger && onlyButton <= abs(fromSmaller)) {
        printf("%d", onlyButton);
    } else if (fromBigger <= onlyButton && fromBigger <= abs(fromSmaller)) {
        printf("%d", fromBigger);
    } else {
        printf("%d", fromSmaller);
    }

    return 0;
}