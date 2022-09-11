#include <stdio.h>
#include <queue>
#include <vector>
#include <utility>

#define EMPTY 0
#define WALL 1
#define DOOR 2

using namespace std;

int isVisited[102][102][3], board[102][102];
int T, h, w, drdc[4][2] = {
    {-1, 0},
    {0, 1},
    {1, 0},
    {0, -1}
};
vector<int> res, abr, abc;

int isInIndex(int row, int col) {
    if (row >= 0 && row < h && col >= 0 && col < w) return 1;
    return 0;
}

void bfs() {
    queue<pair<int, int> > q;
    int nowR, nowC, nextR, nextC, nextCost;

    for (int t = 0; t < 3; ++t) {
        // Initialize isVisited
        for (int r = 0; r <= h + 1; ++r) {
            for (int c = 0; c <= w + 1; ++c) {
                isVisited[r][c][t] = -1;
            }
        }

        q.push(make_pair(abr[0], abc[0]));
        isVisited[abr[0]][abc[0]][t] = 0;

        while (!q.empty()) {
            nowR = q.front().first;
            nowC = q.front().second;
            q.pop();

            for (int i = 0; i < 4; ++i) {
                nextR = nowR + drdc[i][0];
                nextC = nowC + drdc[i][1];
                nextCost = isVisited[nowR][nowC][t];

                if (isInIndex(nextR, nextC) == 1) {
                    if (board[nextR][nextC] == WALL) continue;
                    else if (board[nextR][nextC] == DOOR) ++nextCost;

                    if (isVisited[nextR][nextC][t] == -1 || nextCost < isVisited[nextR][nextC][t]) {
                        isVisited[nextR][nextC][t] = nextCost;
                        q.push(make_pair(nextR, nextC));
                    }
                }
            }
        }
    }

    for (int t = 0; t < 3; ++t) {
        for (int r = 1; r <= h; ++r) {
            for (int c = 1; c <= w; ++c) {
                printf("%d ", isVisited[r][c][t]);
            }
            printf("\n");
        }

        printf("\n");
    }
}

int main() {
    char tmp;

    scanf("%d\n", &T);

    for (int i = 0; i < T; ++T) {
        scanf("%d %d\n", &h, &w);

        abr.push_back(0);
        abc.push_back(0);
        
        for (int r = 1; r <= h; ++r) {
            for (int c = 1; c <= w; ++c) {
                board[r][c] = 0;        
            }
        }

        for (int r = 1; r <= h; ++r) {
            for (int c = 1; c <= w; ++c) {
                scanf("%c", &tmp);

                if (tmp == '.') board[r][c] = EMPTY;
                else if (tmp == '*') board[r][c] = WALL;
                else if (tmp == '#') board[r][c] = DOOR;
                else {
                    abr.push_back(r);
                    abc.push_back(c);
                    board[r][c] = EMPTY;
                }
            }
            scanf("%c", &tmp);
        }

        bfs();
    }
}