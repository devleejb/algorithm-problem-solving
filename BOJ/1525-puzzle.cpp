#include <stdio.h>
#include <queue>
#include <utility>
#include <string>
#include <map>

#define TARGET 123456789

using namespace std;

int board;
int di[4] = {3, -3, 1, -1};
int drdc[4][2] = {
    {-1, 0},
    {0, 1},
    {1, 0},
    {0, -1}
};
map<int, int> isVisitied;

int isInIndex(int r, int c) {
    if (r >= 0 && r < 3 && c >= 0 && c < 3) return 1;
    else return 0;
}

int bfs() {
    queue<pair<int, int> > q;
    string nowBoard, nextBoard;
    int nowCost, nowIdx, nextIdx, nowR, nowC, nextR, nextC;
    char tmp;

    q.push(make_pair(board, 0));
    isVisitied[board] = 1;

    while (!q.empty()) {
        nowBoard = to_string(q.front().first);
        nowCost = q.front().second;
        nowIdx = nowBoard.find('9');
        nowR = nowIdx / 3;
        nowC = nowIdx % 3;
        q.pop();

        for (int i = 0; i < 4; ++i) {
            nextR = nowR + drdc[i][0];
            nextC = nowC + drdc[i][1];
            nextIdx = nextR * 3 + nextC;

            if (isInIndex(nextR, nextC) == 1) {
                nextBoard = nowBoard;
                nextIdx = nextR * 3 + nextC;
                // Swap
                tmp = nextBoard[nextIdx];
                nextBoard[nextIdx] = nextBoard[nowIdx];
                nextBoard[nowIdx] = tmp;
            } else {
                continue;
            }

            if (isVisitied[stoi(nextBoard)] == 0) {
                // printf("%s %d %d\n", nextBoard.c_str(), nowIdx, nextIdx);

                q.push(make_pair(stoi(nextBoard), nowCost + 1));
                isVisitied[stoi(nextBoard)] = 1;

                if (stoi(nextBoard) == TARGET) return nowCost + 1;
            }
        }
    }

    return -1;
}

int main() {
    int tmp;

    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            scanf("%d", &tmp);

            if (tmp == 0) tmp = 9;

            board *= 10;
            board += tmp;
        }
    }

    if (board == TARGET) {
        printf("0");
        return 0;
    }

    printf("%d", bfs());

    return 0;
}