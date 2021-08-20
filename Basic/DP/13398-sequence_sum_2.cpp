#include <stdio.h>

using namespace std;

int N, maxVal;
int seq[100000], dp[100000][2];

void seqSum() {
    dp[0][0] = seq[0];
    dp[0][1] = 0;

    maxVal = seq[0];

    for (int i = 1; i < N; ++i) {
        dp[i][0] = seq[i];

        if (dp[i - 1][0] > 0) {
            dp[i][0] += dp[i - 1][0];
        }

        if (dp[i][0] > maxVal) {
            maxVal = dp[i][0];
        }

        if (dp[i - 1][0] > dp[i - 1][1] + seq[i]) {
            dp[i][1] = dp[i - 1][0];
        } else {
            dp[i][1] = dp[i - 1][1] + seq[i];
        }

        if (dp[i][1] > maxVal) {
            maxVal = dp[i][1];
        }
    }
}

int main() {
    scanf("%d", &N);

    for (int i = 0; i < N; ++i) {
        scanf("%d", &seq[i]);
    }

    seqSum();

    printf("%d", maxVal);

    return 0;
}