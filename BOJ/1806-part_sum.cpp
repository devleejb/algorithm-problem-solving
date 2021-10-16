#include <stdio.h>

using namespace std;

int N, S, minLen = 123456789;
int arr[100000];

void twoPointers() {
    int end = 0, sum = 0, length;

    for (int start = 0; start < N; ++start) {
        while (end < N && sum < S) {
            sum += arr[end++];
        }

        if (sum >= S) {
            length = end - start;

            if (length < minLen) minLen = length;
        }

        sum -= arr[start];
    }
}

int main() {
    scanf("%d %d", &N, &S);

    for (int i = 0; i < N; ++i) {
        scanf("%d", &arr[i]);     
    }

    twoPointers();

    if (minLen == 123456789) minLen = 0;

    printf("%d", minLen);

    return 0;
}