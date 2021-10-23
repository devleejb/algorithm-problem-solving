#include <stdio.h>
#include <queue>
#include <vector>
#include <string>

using namespace std;

int T, N;
int isVisited[20001], from[20001], what[20001];
vector<string> res;

string makeNum(int fromIdx) {
    if (fromIdx == 1) return "1";
    else {
        return makeNum(from[fromIdx]) + to_string(what[fromIdx]);
    }
}

void bfs() {
    queue<int> q;
    int nowNum, num, nextNum[2];

    q.push(1);
    isVisited[1] = 1;
    from[1] = -1;
    what[1] = 1;
    
    while (!q.empty()) {
        nowNum = q.front();
        q.pop();

        nextNum[0] = (nowNum * 10) % N;
        nextNum[1] = (nowNum * 10 + 1) % N;

        for (int i = 0; i < 2; ++i) {
            num = nextNum[i];

            if (isVisited[num] == 0) {
                isVisited[num] = 1;
                from[num] = nowNum;
                what[num] = i;

                q.push(num);

                if (num == 0) return;
            }
        }
    }
}

int main() {
    scanf("%d", &T);

    for (int i = 0; i < T; ++i) {
        scanf("%d", &N);

        fill(isVisited, isVisited + N + 1, 0);
        fill(from, from + N + 1, 0);
        fill(what, what + N + 1, 0);

        bfs();
        res.push_back(makeNum(0));
    }

    for (int i = 0; i < T; ++i) {
        printf("%s\n", res[i].c_str());
    }

    return 0;
}