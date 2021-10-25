#include <stdio.h>
#include <queue>
#include <utility>

using namespace std;

int N, K;
int map[2][100001], isVisited[2][100001];

int bfs() {
    queue<pair<pair<int, int>, int> > q;
    int nowLine, nowPos, nowTime;

    q.push(make_pair(make_pair(0, 1), 0));
    isVisited[0][1] = 1;

    while (!q.empty()) {
        nowLine = q.front().first.first;
        nowPos = q.front().first.second;
        nowTime = q.front().second;
        q.pop();

        if (nowPos + 1 > N || nowPos + K > N) return 1;

        if (nowPos + 1 > nowTime + 1 && isVisited[nowLine][nowPos + 1] == 0 && map[nowLine][nowPos + 1] == 1) {
            isVisited[nowLine][nowPos + 1] = 1;
            q.push(make_pair(make_pair(nowLine, nowPos + 1), nowTime + 1));
        }

        if (nowPos - 1 > nowTime + 1 && isVisited[nowLine][nowPos - 1] == 0 && map[nowLine][nowPos - 1] == 1) {
            isVisited[nowLine][nowPos - 1] = 1;
            q.push(make_pair(make_pair(nowLine, nowPos - 1), nowTime + 1));
        }

        if (nowPos + K > nowTime + 1 && isVisited[!nowLine][nowPos + K] == 0 && map[!nowLine][nowPos + K] == 1) {
            isVisited[!nowLine][nowPos + K] = 1;
            q.push(make_pair(make_pair(!nowLine, nowPos + K), nowTime + 1));
        }
    }

    return 0;
}

int main() {
    scanf("%d %d", &N, &K);

    for (int i = 0; i < 2; ++i) {
        for (int j = 1; j <= N; ++j) {
            scanf("%1d", &map[i][j]);
        }
    }

    printf("%d", bfs());

    return 0;
}