#include <stdio.h>
#include <vector>
#include <map>
#include <queue>
#include <string>

using namespace std;

vector<int> ABC;
int cVisited[201];
int fromTo[6][2] = {
    {0, 1},
    {0, 2},
    {1, 0},
    {1, 2},
    {2, 0},
    {2, 1}
};

string waterToString(vector<int> ABC) {
    string waterStr = "";

    for (int i = 0; i < 3; ++i) {
        if (ABC[i] < 10) waterStr += "00" + to_string(ABC[i]);
        else if (ABC[i] < 100) waterStr += "0" + to_string(ABC[i]);
        else waterStr += to_string(ABC[i]);
    }

    return waterStr;
}

void bfs() {
    queue<vector<int> > q;
    vector<int> nowWater, nextWater;
    string nextWaterStr;
    map<string, int> isVisited;
    int from, to;

    nowWater.resize(3);
    nowWater[2] = ABC[2];
    isVisited[waterToString(nowWater)] = 1;
    cVisited[ABC[2]] = 1;
    q.push(nowWater);

    while (!q.empty()) {
        nowWater = q.front();
        q.pop();

        for (int i = 0; i < 6; ++i) {
            nextWater = nowWater;
            from = fromTo[i][0];
            to = fromTo[i][1];

            nextWater[to] += nextWater[from];

            if (nextWater[to] > ABC[to]) {
                nextWater[from] = nextWater[to] - ABC[to];
                nextWater[to] = ABC[to];
            } else {
                nextWater[from] = 0;
            }

            nextWaterStr = waterToString(nextWater);

            if (isVisited[nextWaterStr] == 0) {
                isVisited[nextWaterStr] = 1;
                q.push(nextWater);

                if (nextWater[0] == 0) cVisited[nextWater[2]] = 1;
            }
        }
    }
}

int main() {
    ABC.resize(3);

    for (int i = 0; i < 3; ++i) scanf("%d", &ABC[i]);

    bfs();

    for (int i = 0; i <= ABC[2]; ++i) {
        if (cVisited[i] == 1) printf("%d ", i);
    }

    return 0;
}