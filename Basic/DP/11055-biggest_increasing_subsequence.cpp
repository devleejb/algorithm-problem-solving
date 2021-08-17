#include <stdio.h>

using namespace std;

int N, maxVal;
int A[1001], dp[1001];

int calLIS() {
    for (int i = 1; i <= N; ++i) {
        dp[i] = A[i];

        for (int j = 1; j < i; ++j) {
            if (A[j] < A[i] && dp[j] + A[i] > dp[i]) {
                dp[i] = dp[j] + A[i];
            }
        }

        if (maxVal < dp[i]) maxVal = dp[i];
    }

    return maxVal;
}

int main() {
    scanf("%d", &N);

    for (int i = 1; i <= N; ++i) {
        scanf("%d", &A[i]);
    }

    printf("%d", calLIS());

    return 0;
}