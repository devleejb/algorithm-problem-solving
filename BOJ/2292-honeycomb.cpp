#include <stdio.h>

using namespace std;

int N, cnt = 1;

void honeyComb() {
    int sum = 1;

    while (sum < N) {
        sum += cnt * 6;
        ++cnt;
    }
}

int main() {
    scanf("%d", &N);

    honeyComb();

    printf("%d", cnt);

    return 0;
}