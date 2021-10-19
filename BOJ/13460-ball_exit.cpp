#include <stdio.h>
#include <utility>
#include <queue>

using namespace std;

int N, M, rRow, rCol, bRow, bCol, tRow, tCol;
int board[11][11], drdc[4][2] = {
    {-1, 0},
    {0, 1},
    {1, 0},
    {0, -1}
};

pair<pair<pair<int, int>, pair<int, int> >, pair<int, int> > move(int nowRRow, int nowRCol, int nowBRow, int nowBCol, int orientation) {
    int RHoleSignal = 0, BHoleSignal = 0, nextRRow = nowRRow, nextRCol = nowRCol, nextBRow = nowBRow, nextBCol = nowBCol;

    if (orientation == 0) {
        // Up
        while (board[nextRRow - 1][nextRCol] != 0) {
            --nextRRow;
            if (tRow == nextRRow && tCol == nextRCol) RHoleSignal = 1;
        }
        while (board[nextBRow - 1][nextBCol] != 0) {
            --nextBRow;
            if (tRow == nextBRow && tCol == nextBCol) BHoleSignal = 1;
        }

        if (nextRRow == nextBRow && nextRCol == nextBCol) {
            if (nowRRow > nowBRow) ++nextRRow;
            else ++nextBRow;
        }
    } else if (orientation == 1) {
        // right
        while (board[nextRRow][nextRCol + 1] != 0) {
            ++nextRCol;
            if (tRow == nextRRow && tCol == nextRCol) RHoleSignal = 1;
        }
        while (board[nextBRow][nextBCol + 1] != 0) {
            ++nextBCol;
            if (tRow == nextBRow && tCol == nextBCol) BHoleSignal = 1;
        }
        if (nextRRow == nextBRow && nextRCol == nextBCol) {
            if (nowRCol > nowBCol) --nextBCol;
            else --nextRCol;
        }
    } else if (orientation == 2) {
        // left
        while (board[nextRRow][nextRCol - 1] != 0) {
            --nextRCol;
            if (tRow == nextRRow && tCol == nextRCol) RHoleSignal = 1;
        }
        while (board[nextBRow][nextBCol - 1] != 0) {
            --nextBCol;
            if (tRow == nextBRow && tCol == nextBCol) BHoleSignal = 1;
        }
        if (nextRRow == nextBRow && nextRCol == nextBCol) {
            if (nowRCol > nowBCol) ++nextRCol;
            else ++nextBCol;
        }
    } else {
        // down
        while (board[nextRRow + 1][nextRCol] != 0) {
            ++nextRRow;
            if (tRow == nextRRow && tCol == nextRCol) RHoleSignal = 1;
        }
        while (board[nextBRow + 1][nextBCol] != 0) {
            ++nextBRow;
            if (tRow == nextBRow && tCol == nextBCol) BHoleSignal = 1;
        }
        if (nextRRow == nextBRow && nextRCol == nextBCol) {
            if (nowRRow > nowBRow) --nextBRow;
            else --nextRRow;
        }
    }

    return make_pair(make_pair(make_pair(nextRRow, nextRCol), make_pair(nextBRow, nextBCol)), make_pair(RHoleSignal, BHoleSignal));
}

void bfs() {
    queue<pair<pair<int, int>, int> > rq;
    queue<pair<int, int> > bq;
    pair<pair<pair<int, int>, pair<int, int> >, pair<int, int> > afterMove;
    int nowRRow, nowRCol, nowBRow, nowBCol, nowCost, nextRRow,nextRCol, nextBRow, nextBCol, RHoleSignal, BHoleSignal;

    rq.push(make_pair(make_pair(rRow, rCol), 0));
    bq.push(make_pair(bRow, bCol));

    while (!rq.empty()) {
        pair<pair<int, int>, int> red = rq.front();
        pair<int, int> blue = bq.front();
        
        nowRRow = red.first.first;
        nowRCol = red.first.second;
        nowCost = red.second;
        nowBRow = blue.first;
        nowBCol = blue.second;

        rq.pop();
        bq.pop();

        if (nowCost == 10) {
            printf("-1");
            return;
        }

        for (int i = 0; i < 4; ++i) {
            afterMove = move(nowRRow, nowRCol, nowBRow, nowBCol, i);
            nextRRow = afterMove.first.first.first;
            nextRCol = afterMove.first.first.second;
            nextBRow = afterMove.first.second.first;
            nextBCol = afterMove.first.second.second;
            RHoleSignal = afterMove.second.first;
            BHoleSignal = afterMove.second.second;

            if (RHoleSignal == 1 && BHoleSignal == 0) {
                printf("%d", nowCost + 1);
                return;
            } else if (RHoleSignal == 0 && BHoleSignal == 0) {
                rq.push(make_pair(make_pair(nextRRow, nextRCol), nowCost + 1));
                bq.push(make_pair(nextBRow, nextBCol));
            }
        }
    }
}

int main() {
    char tmp;

    scanf("%d %d\n", &N, &M);

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            scanf("%c", &tmp);

            if (tmp == '#') board[i][j] = 0;
            else if (tmp == '.') board[i][j] = 1;
            else if (tmp == 'R') {
                board[i][j] = 1;
                rRow = i;
                rCol = j;
            } else if (tmp == 'B') {
                board[i][j] = 1;
                bRow = i;
                bCol = j;
            } else {
                board[i][j] = 1;
                tRow = i;
                tCol = j;
            }
        }

        scanf("%c", &tmp);
    }

    bfs();

    return 0;
}