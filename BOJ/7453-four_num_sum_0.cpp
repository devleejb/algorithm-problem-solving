#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

int n;
int A[4000], B[4000], C[4000], D[4000];
vector<long long> leftSum, rightSum;
long long cnt;

void count() {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j){
            leftSum.push_back(A[i] + B[j]);
            rightSum.push_back(C[i] + D[j]);
        }
    }

    sort(rightSum.begin(), rightSum.end());

    for (int i = 0; i < leftSum.size(); ++i) {
        int diff = -leftSum[i];

        cnt += upper_bound(rightSum.begin(), rightSum.end(), diff) - lower_bound(rightSum.begin(), rightSum.end(), diff);
    }
}

int main() {
    scanf("%d", &n);

    for (int i = 0; i < n; ++i) {
        scanf("%d", &A[i]);
        scanf("%d", &B[i]);
        scanf("%d", &C[i]);
        scanf("%d", &D[i]);
    }

    count();

    printf("%lld", cnt);

    return 0;
}