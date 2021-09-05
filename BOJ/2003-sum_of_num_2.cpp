#include <stdio.h>

using namespace std;

int N, M, cnt;
int series[30001], sum[30001];

void sumSeries() {
    for (int i = 1; i <= N; ++i) {
        sum[i] = sum[i - 1] + series[i]; 
    }
}

void countCase() {
    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j <= N; ++j) {
            if (sum[j] - sum[i] == M) {
                ++cnt;
            }
        }
    }
}

int main() {
    scanf("%d %d", &N, &M);

    for (int i = 1; i <= N; ++i) {
        scanf("%d", &series[i]);
    }

    sumSeries();
    countCase();

    printf("%d", cnt);

    return 0;
}