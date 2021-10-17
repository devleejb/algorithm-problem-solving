#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int T, n, m;
long long cnt;
vector<int> A, B;
vector<long long> ASum, BSum;


void calculateCnt() {
    long long sum;

    for (int i = 0; i < n; ++i) {
        sum = 0;
        
        for (int j = i; j < n; ++j) {
            sum += A[j];
            ASum.push_back(sum);
        }
    }

    for (int i = 0; i < m; ++i) {
        sum = 0;
        
        for (int j = i; j < m; ++j) {
            sum += B[j];
            BSum.push_back(sum);
        }
    }

    sort(BSum.begin(), BSum.end());

    for (int i = 0; i < ASum.size(); ++i) {
        long long diff = T - ASum[i];

        cnt += upper_bound(BSum.begin(), BSum.end(), diff) - lower_bound(BSum.begin(), BSum.end(), diff);
    }
}

int main() {
    scanf("%d %d", &T, &n);

    A.resize(n);

    for (int i = 0; i < n; ++i) {
        scanf("%d", &A[i]);
    }

    scanf("%d", &m);

    B.resize(m);

    for (int i = 0; i < m; ++i) {
        scanf("%d", &B[i]);
    }

    calculateCnt();

    printf("%lld", cnt);

    return 0;
}
