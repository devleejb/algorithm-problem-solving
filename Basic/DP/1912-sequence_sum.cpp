#include <stdio.h>

using namespace std;

int N, max;
int seq[100000], dp[100000];

void sequenceSum() {
    max = seq[0];
    dp[0] = seq[0];

    for (int i = 1; i < N; ++i) {
        dp[i] = seq[i];

        if (dp[i - 1] > 0) {
            dp[i] += dp[i - 1];
        }

        if (max < dp[i]) {
            max = dp[i];
        }
    }
}

int main() {
    scanf("%d", &N);

    for (int i = 0; i < N; ++i) {
        scanf("%d", &seq[i]);
    }

    sequenceSum();

    printf("%d", max);

    return 0;
}