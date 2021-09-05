#include <stdio.h>
#include <math.h>

using namespace std;

int N;
int dp[100001];

void sumOfSuared() {
    for (int i = 1; i <= N; ++i) {
        dp[i] = i;

        for (int j = 1; j <= sqrt(i); ++j) {
            if (dp[i - j * j] + 1 < dp[i]) {
                dp[i] = dp[i - j * j] + 1;
            }
        }
    }
}

int main() {
    scanf("%d", &N);

    sumOfSuared();

    printf("%d", dp[N]);

    return 0;
}