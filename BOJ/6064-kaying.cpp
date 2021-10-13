#include <stdio.h>
#include <vector>

using namespace std;

vector<int> M, N, X, Y, result;
int T;

void kaying(int c) {
    int nowM = M[c], nowN = N[c], targetX = X[c], targetY = Y[c], cntX = 1, cntY = 1;

    if (targetX > nowM || targetY > nowN) {
        result.push_back(-1);
        return;
    } else if (targetX == 1 && targetY == 1) {
        result.push_back(0);
        return;
    }

    cntX = targetX;
    cntY = targetY;

    while (cntX != cntY && cntX < nowM * nowN && cntY < nowM * nowN) {
        if (cntX < cntY) {
            cntX += nowM;
        } else {
            cntY += nowN;
        }
    }

    if (cntX >= nowM * nowN || cntY >= nowM * nowN) {
        result.push_back(-1);
    } else {
        result.push_back(cntX); 
    }
}

int main() {
    int tmpM, tmpN, tmpX, tmpY;

    scanf("%d", &T);

    for (int i = 0; i < T; ++i) {
        scanf("%d %d %d %d", &tmpM, &tmpN, &tmpX, &tmpY);
        M.push_back(tmpM);
        N.push_back(tmpN);
        X.push_back(tmpX);
        Y.push_back(tmpY);
        
        kaying(i);
    }

    for (int i = 0; i < T; ++i) {
        printf("%d\n", result[i]);
    }

    return 0;
}