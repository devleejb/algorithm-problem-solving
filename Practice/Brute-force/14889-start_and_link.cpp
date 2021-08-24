#include <stdio.h>
#include <vector>
#include <cmath>

using namespace std;

int N, minDif = 40000, tmp, sum;
int stat[20][20], isSelected[20], isSelectedInTeam[20];
vector<int> team, pairs;

int calStat(int teamNum) {
    int sum = 0;

    if (pairs.size() == 2) {
        return stat[pairs[0]][pairs[1]] + stat[pairs[1]][pairs[0]];
    } else {
        for (int i = 0; i < N; ++i) {
            if (isSelected[i] == teamNum && isSelectedInTeam[i] == 0 && (pairs.size() == 0 || pairs[0] < i)) {
                isSelectedInTeam[i] = 1;
                pairs.push_back(i);
                
                sum += calStat(teamNum);

                isSelectedInTeam[i] = 0;
                pairs.pop_back();
            }
        }
    }

    return sum;
}



void calMinDif() {
    if (team.size() == N / 2) {
        int val = abs(calStat(0) - calStat(1));

        if (val < minDif) minDif = val;
    } else {
        for (int i = 0; i < N; ++i) {
            if (isSelected[i] == 0 && (team.size() == 0 || i > team[team.size() - 1])) {
                isSelected[i] = 1;
                team.push_back(i);
                
                calMinDif();

                isSelected[i] = 0;
                team.pop_back();
            }
        }
    }
}

int main() {
    scanf("%d", &N);

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            scanf("%d", &tmp);

            sum += tmp;

            stat[i][j] = tmp;
        }
    }
    
    calMinDif();

    printf("%d", minDif);

    return 0;
}