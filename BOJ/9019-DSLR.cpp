#include <stdio.h>
#include <queue>
#include <string>
#include <algorithm>

using namespace std;

queue<string> res; 
int T, A, B;
int isVisited[10000];

int D(int n) {
    return (n * 2) % 10000;
}

int S(int n) {
    --n;

    if (n == -1) return 9999;
    else return n;
}

int L(int n) {
    int first = n / 1000;

    n = n - first * 1000;
    n *= 10;
    n += first;

    return n;
}

int R(int n) {
    int last = n % 10;

    n /= 10;
    n += last * 1000;

    return n;
}

void bfs() {
    queue<int> q;
    int nowNum, tmpNum;
    string tmpStr;

    q.push(A);
    isVisited[A] = A;

    while (!q.empty()) {
        nowNum = q.front();
        q.pop();

        if (isVisited[tmpNum = D(nowNum)] == -1) {
            q.push(tmpNum);
            isVisited[tmpNum] = nowNum;
            if (tmpNum == B) break;
        }

        if (isVisited[tmpNum = S(nowNum)] == -1) {
            q.push(tmpNum);
            isVisited[tmpNum] = nowNum;
            if (tmpNum == B) break;
        }

        if (isVisited[tmpNum = L(nowNum)] == -1) {
            q.push(tmpNum);
            isVisited[tmpNum] = nowNum;
            if (tmpNum == B) break;
        }

        if (isVisited[tmpNum = R(nowNum)] == -1) {
            q.push(tmpNum);
            isVisited[tmpNum] = nowNum;
            if (tmpNum == B) break;
        }
    }
    
    tmpNum = B;
    tmpStr = "";

    while (tmpNum != A) {
        int num = isVisited[tmpNum];

        if (tmpNum == D(num)) tmpStr += "D";
        else if (tmpNum == S(num)) tmpStr += "S";
        else if (tmpNum == L(num)) tmpStr += "L";
        else if (tmpNum == R(num)) tmpStr += "R";

        tmpNum = num;
    }

    reverse(tmpStr.begin(), tmpStr.end());
    res.push(tmpStr);
}

int main() {
    scanf("%d", &T);

    for (int i = 0; i < T; ++i) {
        scanf("%d %d", &A, &B);
        for (int i = 0; i < 10000; ++i) isVisited[i] = -1;
        bfs();
    }

    for (int i = 0; i < T; ++i) {
        printf("%s\n", res.front().c_str());
        res.pop();
    }

    return 0;
}