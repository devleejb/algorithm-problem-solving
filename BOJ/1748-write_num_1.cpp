#include <stdio.h>
#include <cmath>

using namespace std;

int N, digit = 1, digitSum;

void calDigit() {
    int divider = 10, nowNum;

    while (N / divider >= 1) {
        digitSum += digit * 9 * pow(10, digit - 1);

        ++digit;
        divider *= 10;
    }

    nowNum = pow(10, digit - 1);
    digitSum += digit;

    while ( nowNum != N ) {
        digitSum += digit;
        ++nowNum;
    }
    
}

int main() {
    scanf("%d", &N);

    calDigit();

    printf("%d", digitSum);

    return 0;
}