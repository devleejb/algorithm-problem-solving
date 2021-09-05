#include <stdio.h>
#include <stack>

using namespace std;

int N, maxIdx;
int A[1001], dp[1001], prevIdx[1001];

void calLIS() {
    int tmp;
    stack<int> s;

    maxIdx = 1;

    for (int i = 1; i <= N; ++i) {
        dp[i] = 1;
        prevIdx[i] = i;

        for (int j = 1; j < i; ++j) {
            if (A[j] < A[i] && dp[j] + 1 > dp[i]) {
                dp[i] = dp[j] + 1;
                prevIdx[i] = j;

                if (dp[maxIdx] < dp[i]) maxIdx = i;
            }
        }
    }

    printf("%d\n", dp[maxIdx]);

    while (maxIdx != prevIdx[maxIdx]) {
        s.push(A[maxIdx]);

        maxIdx = prevIdx[maxIdx];
    }

    s.push(A[maxIdx]);

    while (!s.empty()) {
        tmp = s.top();
        s.pop();

        printf("%d ", tmp);
    }
}

int main() {
    scanf("%d", &N);

    for (int i = 1; i <= N; ++i) {
        scanf("%d", &A[i]);
    }

    calLIS();

    return 0;
}