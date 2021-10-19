#include <stdio.h>
#include <stdlib.h>

using namespace std;

int board[9][9];

int isAvailable(int row, int col) {
    int isUsedInRow[10] = {0}, isUsedInCol[10] = {0}, isUsedInBlock[10] = {0};

    for (int i = 0; i < 9; ++i) {
        int num = board[row][i];

        if (num != 0) {
            if (isUsedInRow[num] == 0) {
                isUsedInRow[num] = 1;
            } else {
                return 0;
            }
        }
    }

    for (int i = 0; i < 9; ++i) {
        int num = board[i][col];

        if (num != 0) {
            if (isUsedInCol[num] == 0) {
                isUsedInCol[num] = 1;
            } else {
                return 0;
            }
        }
    }

    for (int i = row / 3 * 3; i < row / 3 * 3 + 3; ++i) {
        for (int j = col / 3 * 3; j < col / 3 * 3 + 3; ++j) {
            int num = board[i][j];

            if (num != 0) {
                if (isUsedInBlock[num] == 0) {
                    isUsedInBlock[num] = 1;
                } else {
                    return 0;
                }
            }
        }
    }

    return 1;
}

void makeBoard(int row, int col) {
    if (row == 9) {
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                printf("%d ", board[i][j]);
            }
            printf("\n");
        }

        exit(0);
    }

    int nextRow = row, nextCol = col + 1;

    if (nextCol == 9) {
        ++nextRow;
        nextCol = 0;
    }

    if (board[row][col] == 0) {
        for (int i = 1; i < 10; ++i) {
            board[row][col] = i;
            if (isAvailable(row, col)) {
                makeBoard(nextRow, nextCol);
            }
            board[row][col] = 0;
        }
    } else {
        makeBoard(nextRow, nextCol);
    }
}

int main() {
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            scanf("%d", &board[i][j]);
        }
    }

    makeBoard(0, 0);

    return 0;
}