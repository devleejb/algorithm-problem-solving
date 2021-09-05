#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

int N, M, maxSum;
int score[4][4], isUsed[4][4];

void paperSlice(int x, int y, int sumScore) {
    int nextX, nextY, slicedNum, toIdx;

    if (y >= N) {
        if (sumScore > maxSum) {
            maxSum = sumScore;
        }

        return;
    }

    nextX = x + 1;
    nextY = y;

    if (nextX >= M) {
        nextX = 0;
        ++nextY;
    }

    if (isUsed[y][x] == 1) {
        paperSlice(nextX, nextY, sumScore);

        return;
    }

    slicedNum = 0;

    for (toIdx = x; toIdx < M; ++toIdx) {
        if (isUsed[y][toIdx] == 0) {
            isUsed[y][toIdx] = 1;
            slicedNum *= 10;
            slicedNum += score[y][toIdx];

            paperSlice(nextX, nextY, sumScore + slicedNum);
        } else {
            break;
        }
    }

    for (int i = x; i < toIdx; ++i) {
        isUsed[y][i] = 0;
    }

    slicedNum = 0;

    for (toIdx = y; toIdx < N; ++toIdx) {
        if (isUsed[toIdx][x] == 0) {
            isUsed[toIdx][x] = 1;
            slicedNum *= 10;
            slicedNum += score[toIdx][x];

            paperSlice(nextX, nextY, sumScore + slicedNum);
        } else {
            break;
        }
    }

    for (int i = y; i < toIdx; ++i) {
        isUsed[i][x] = 0;
    }
}

int main() {
    string tmp;

    scanf("%d %d", &N, &M);

    for (int i = 0; i < N; ++i) {
        cin >> tmp;

        for (int j = 0; j < M; ++j) {
            score[i][j] = tmp[j] - '0';
        }
    }

    paperSlice(0, 0, 0);

    printf("%d", maxSum);

    return 0;
}