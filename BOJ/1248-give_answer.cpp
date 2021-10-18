#include <stdio.h>
#include <vector>

using namespace std;

int N, endSignal;
int iSum[10][10], input[10][10];
vector<int> now, ans;

int isAvailable(int idx) {
    int sign;

    for (int i = 0; i <= idx; ++i) {
        sign = input[i][idx];

        if (sign == 1 && iSum[i][idx] <= 0) return 0;
        else if (sign == 0 && iSum[i][idx] != 0) return 0;
        else if (sign == -1 && iSum[i][idx] >= 0) return 0;    
    }

    return 1;
}

void makeISum(int idx) {
    for (int i = 0; i <= idx; ++i) {
        if (i == idx) {
            iSum[i][i] = now[idx];
        } else {
            iSum[i][idx] = iSum[i][idx - 1] + now[idx];
        }
    }
}

void makeNumber(int idx) {
    if (endSignal == 1) {
        return;
    }

    if (idx == N) {
        ans = now;
        endSignal = 1;
        return;
    }

    if (input[idx][idx] == 0) {
        now.push_back(0);
        makeISum(idx);
        makeNumber(idx + 1);
        now.pop_back();
    } else {
        int sign = input[idx][idx];

        for (int i = 1; i <= 10; ++i) {
            now.push_back(sign * i);
            makeISum(idx);

            if (isAvailable(idx)) {
                makeNumber(idx + 1);
            }

            now.pop_back();
        }
    }
}

int main() {
    char tmp;

    scanf("%d\n", &N);

    for (int i = 0; i < N; ++i) {
        for (int j = i; j < N; ++j) {
            scanf("%c", &tmp);

            if (tmp == '0') {
                input[i][j] = 0;
            } else if (tmp == '+') {
                input[i][j] = 1;
            } else {
                input[i][j] = -1;
            }
        }
    }

    makeNumber(0);

    for (int i = 0; i < N; ++i) {
        printf("%d ", ans[i]);
    }

    return 0;
}