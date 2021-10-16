#include <stdio.h>
#include <map>

using namespace std;

map<int, int> m;
int N, S, half;
int arr[41];
long long cnt;

void subseriesSumLeft(int idx, int sum) {
    if (idx == half) {
        m[sum]++;
        return;
    }

    subseriesSumLeft(idx + 1, sum);
    subseriesSumLeft(idx + 1, sum + arr[idx]);
}

void subseriesSumRight(int idx, int sum) {
    if (idx == N) {
        cnt += m[S - sum];
        return;
    }

    subseriesSumRight(idx + 1, sum);
    subseriesSumRight(idx + 1, sum + arr[idx]);
}

int main() {
    scanf("%d %d", &N, &S);

    for (int i = 0; i < N; ++i) {
        scanf("%d", &arr[i]);
    }

    half = N / 2;

    subseriesSumLeft(0, 0);
    subseriesSumRight(half, 0);

    if (S == 0) --cnt;

    printf("%lld", cnt);

    return 0 ;
}