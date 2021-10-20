#include <stdio.h>
#include <queue>
#include <vector>
#include <utility>

using namespace std;

int isVisited[100001];
int N, K, cost;

void bfs() {
    queue<pair<int, int> > q;

    q.push(make_pair(N, 0));
    isVisited[N] = 1;

    while (!q.empty()) {
        int nowPos = q.front().first;
        int nowCost = q.front().second;

        q.pop();

        if (isVisited[nowPos + 1] == -1) {
            isVisited[nowPos + 1] = nowPos;
            q.push(make_pair(nowPos + 1, nowCost + 1));
        }

        if (isVisited[nowPos - 1] == -1) {
            isVisited[nowPos - 1] = nowPos;
            q.push(make_pair(nowPos - 1, nowCost + 1));
        }

        if (nowPos * 2 < 100001 && isVisited[nowPos * 2] == -1) {
            isVisited[nowPos * 2] = nowPos;
            q.push(make_pair(nowPos * 2, nowCost + 1));
        }

        if (nowPos + 1 == K || nowPos - 1 == K || nowPos * 2 == K) {
            cost = nowCost + 1;
            return;
        }
    }
}

int main() {
    int idx;
    vector<int> path;

    scanf("%d %d", &N, &K);

    for (int i = 0; i < 100001; ++i) {
        isVisited[i] = -1;
    }

    if (N == K) {
        printf("0\n%d", N);
        return 0;
    }

    bfs();

    printf("%d\n", cost);

    idx = K;

    while (idx != N) {
        path.push_back(idx);
        idx = isVisited[idx];
    }

    path.push_back(idx);

    for (int i = path.size() - 1; i >= 0; --i) {
        printf("%d ", path[i]);
    }

    return 0;
}