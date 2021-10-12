#include <stdio.h>
#include <vector>
#include <math.h>

using namespace std;

int N, cnt;
int isNotPrime[4000001];
vector<int> primes;

void eratos() {
    for (int i = 2; i <= sqrt(N); ++i) {
        if (isNotPrime[i] == 0) {
            int j = 2; 

            while (i * j <= N) {
                isNotPrime[i * j] = 1;
                ++j;
            }
        }
    }

    for (int i = 2; i <= N; ++i) {
        if (isNotPrime[i] == 0) {
            primes.push_back(i);
        }
        
    }
}

void twoPointers() {
    int end = 0, sumVal = 0;

    for (int start = 0; start < primes.size(); ++start) {
        while (sumVal < N && end < primes.size()) {
            sumVal += primes[end++];
        }

        if (sumVal == N) ++cnt;

        sumVal -= primes[start];
    }
}

int main() {
    scanf("%d", &N);

    eratos();
    twoPointers();

    printf("%d", cnt);

    return 0;
}
