#include <stdio.h>

using namespace std;

int N, cnt, selectedChess;
int pos[15], isUsed[15];

int isAvailable(int col, int row) {
    for (int i = 0; i < col; ++i) {
        if (pos[i] == row - (col - i) || pos[i] == row + (col - i)) {
            return 0;
        }
    }

    return 1;
}

void nQueen() {
    if (selectedChess == N) {
        ++cnt;

        return;
    } else {
        for (int i = 0; i < N; ++i) {
            if (isUsed[i] == 0 && isAvailable(selectedChess, i)) {
                isUsed[i] = 1;
                pos[selectedChess] = i;
                ++selectedChess;

                nQueen();

                isUsed[i] = 0;
                --selectedChess;
            }
        }
    }
}

int main() {
    scanf("%d", &N);

    nQueen();

    printf("%d", cnt);

    return 0;
}