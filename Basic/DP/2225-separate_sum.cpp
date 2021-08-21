#include <stdio.h>

using namespace std;

int N, K;
long long sum;
long long dp[201][201];

void separateSum() {
    for (int i = 0; i <= N; ++i) {
        dp[1][i] = 1;
    }

    for (int i = 2; i <= K; ++i) {
        for (int j = 0; j <= N; ++j) {
            sum = 0;

            for (int k = 0; k <= j; ++k) {
                sum += dp[i - 1][k] % 1000000000;
                sum %= 1000000000;
            }

            dp[i][j] = sum;
        }
    }
}

int main() {
    scanf("%d %d", &N, &K);

    separateSum();

    printf("%lld", dp[K][N]);

    return 0;
}