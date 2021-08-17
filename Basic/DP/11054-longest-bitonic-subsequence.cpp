#include <stdio.h>

using namespace std;

int N, maxSum;
int lis[1001], revLis[1001], A[1001];

void calLIS() {
    for (int i = 1; i <= N; ++i) {
        lis[i] = 1;

        for (int j = 1; j < i; ++j) {
            if (A[j] < A[i] && lis[j] + 1 > lis[i]) {
                lis[i] = lis[j] + 1;
            }
        }
    }
}

void calReverseLIS() {
    for (int i = N; i > 0; --i) {
        revLis[i] = 1;

        for (int j = N; j > i; --j) {
            if (A[j] < A[i] && revLis[j] + 1 > revLis[i]) {
                revLis[i] = revLis[j] + 1;
            }
        }
    }
}

void calLBS() {
    int tmpSum;

    for (int i = 1; i <= N; ++i) {
        tmpSum = lis[i] + revLis[i] - 1;

        if (tmpSum > maxSum) maxSum = tmpSum;
    }

    printf("%d", maxSum);
}

int main() {
    scanf("%d", &N);

    for (int i = 1; i <= N; ++i) {
        scanf("%d", &A[i]);
    }

    calLIS();
    calReverseLIS();
    calLBS();

    return 0;
}