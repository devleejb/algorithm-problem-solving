#include <stdio.h>
#include <queue>
#include <utility>

using namespace std;

int isVisited[100001], minCost[100001];
int N, K;

void bfs() {
    queue<pair<int, int> > q;
    int nowPos, nowCost;

    if (N == K) {
        isVisited[N] = 1;
        
        return;
    }

    q.push(make_pair(N, 0));
    isVisited[N] = 1;

    while (!q.empty()) {
        nowPos = q.front().first;
        nowCost = q.front().second;

        q.pop();

        if (minCost[K] != 0 && minCost[K] <= nowCost) return;

        if (nowPos - 1 >= 0 && (isVisited[nowPos - 1] == 0 || minCost[nowPos - 1] == nowCost + 1)) {
            ++isVisited[nowPos - 1];
            minCost[nowPos - 1] = nowCost + 1;
            q.push(make_pair(nowPos - 1, nowCost + 1));
        }

        if (nowPos + 1 <= 100000 && (isVisited[nowPos + 1] == 0 || minCost[nowPos + 1] == nowCost + 1)) {
            ++isVisited[nowPos + 1];
            minCost[nowPos + 1] = nowCost + 1;
            q.push(make_pair(nowPos + 1, nowCost + 1));
        }

        if (nowPos * 2 <= 100000 && (isVisited[nowPos * 2] == 0 || minCost[nowPos * 2] == nowCost + 1)) {
            ++isVisited[nowPos * 2];
            minCost[nowPos * 2] = nowCost + 1;
            q.push(make_pair(nowPos * 2, nowCost + 1));
        }
    }
}

int main() {
    scanf("%d %d", &N, &K);

    bfs();

    printf("%d\n%d", minCost[K], isVisited[K]);

    return 0;
}