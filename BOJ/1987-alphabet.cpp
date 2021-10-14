#include <stdio.h>

using namespace std;

int R, C, maxCnt;
int isPassed[27];
char board[20][20];
int drdc[4][2] = {
    {-1, 0},
    {0, 1},
    {1, 0},
    {0, -1}
};

int isInBoard(int r, int c) {
    if (r < R && r >= 0 && c < C && c >= 0) {
        return 1;
    }

    return 0;
}

void moveHorse(int r, int c, int cnt) {
    if (cnt > maxCnt) maxCnt = cnt;

    for (int i = 0; i < 4; ++i) {
        int nextRow = r + drdc[i][0];
        int nextCol = c + drdc[i][1];

        if (isInBoard(nextRow, nextCol) && isPassed[board[nextRow][nextCol] - 65] == 0) {
            isPassed[board[nextRow][nextCol] - 65] = 1;
            moveHorse(nextRow, nextCol, cnt + 1);
            isPassed[board[nextRow][nextCol] - 65] = 0;
        }
    }
}

int main() {
    char tmpChar;

    scanf("%d %d\n", &R, &C);

    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            scanf("%c", &board[i][j]);
        }
        scanf("%c", &tmpChar);
    }

    isPassed[board[0][0] - 65] = 1;
    moveHorse(0, 0, 1);

    printf("%d", maxCnt);

    return 0;
}