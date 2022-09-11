#include <stdio.h>
#include <queue>
#include <utility>
#include <vector>

#define EMPTY 0
#define WALL 1
#define UP 0
#define RIGHT 1
#define DOWN 2
#define LEFT 3
#define START 4

using namespace std;

int W, H;
int board[101][101], isVisited[101][101], cost[101][101], drdc[4][2] = {
    {-1, 0},
    {0, 1},
    {1, 0},
    {0, -1}
};
vector<int> cr, cc;

int isInIndex(int r, int c) {
    if (r >= 0 && r < H && c >= 0 && c < W) return 1;
    else return 0;
}

void bfs() {
    queue<pair<pair<int, int>, pair<int, int> > > q;
    int nowR, nowC, nowCost, nextCost, nextR, nextC, nowOr;

    q.push(make_pair(make_pair(cr[0], cc[0]), make_pair(START, 0)));
    isVisited[cr[0]][cc[0]] = 1;

    while (!q.empty()) {
        nowR = q.front().first.first;
        nowC = q.front().first.second;
        nowOr = q.front().second.first;
        nowCost = q.front().second.second;
        q.pop();

        for (int i = 0; i < 4; ++i) {
            nextR = nowR + drdc[i][0];
            nextC = nowC + drdc[i][1];

            if (nowOr != START && nowOr != i) nextCost = nowCost + 1;
            else nextCost = nowCost;

            if (isInIndex(nextR, nextC) == 1 && board[nextR][nextC] == EMPTY && (isVisited[nextR][nextC] == 0 || nextCost <= cost[nextR][nextC])) {
                isVisited[nextR][nextC] = 1;
                cost[nextR][nextC] = nextCost;
                q.push(make_pair(make_pair(nextR, nextC), make_pair(i, nextCost)));
            }
        }
    }
}

int main() {
    char tmp;

    scanf("%d %d", &W, &H);
    fflush(stdin);

    for (int r = 0; r < H; ++r) {
        for (int c = 0; c < W; ++c) {
            scanf("%c", &tmp);
        
            if (tmp == '.') board[r][c] = EMPTY;
            else if (tmp == '*') board[r][c] = WALL;
            else if (tmp == 'C') {
                board[r][c] = EMPTY;
                cr.push_back(r);
                cc.push_back(c);
            }
        }
        
        fflush(stdin);
    }

    bfs();

    printf("%d", cost[cr[1]][cc[1]]);

    return 0;
}