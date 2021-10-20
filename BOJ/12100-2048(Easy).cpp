#include <stdio.h>
#include <deque>

using namespace std;

int N, maxVal;
deque<int> board[20];

void move(int orientation) {
    if (orientation == 0 || orientation == 1) {
        // Right : 0, Left : 1
        for (int r = 0; r < N; ++r) {
            deque<int> tmp;
            int cnt = 0;

            for (int c = 0; c < N; ++c) {
                if (board[r][c] == 0) {
                    if (orientation == 0) {
                        tmp.push_front(0);
                    } else if (orientation == 1) {
                        ++cnt;
                    }
                } else {
                    tmp.push_back(board[r][c]);
                }
            }

            if (orientation == 1) {
                for (int i = 0; i < cnt; ++i) tmp.push_back(0);

                for (int i = 0; i < N - 1; ++i) {
                    if (tmp[i] != 0 && tmp[i] == tmp[i + 1]) {
                        tmp[i] *= 2;
                        tmp.erase(tmp.begin() + i + 1);
                        tmp.push_back(0);

                        if (tmp[i] > maxVal) maxVal = tmp[i];
                    }
                }
            } else if (orientation == 0) {
                for (int i = N - 1; i > 0; --i) {
                    if (tmp[i] != 0 && tmp[i] == tmp[i - 1]) {
                        tmp[i] *= 2;
                        tmp.erase(tmp.begin() + i - 1);
                        tmp.push_front(0);

                        if (tmp[i] > maxVal) maxVal = tmp[i];
                    }
                }
            }

            board[r] = tmp;
        }
    }

    if (orientation == 2 || orientation == 3) {
        // Up : 2, Down : 3
        for (int c = 0; c < N; ++c) {
            deque<int> tmp;
            int cnt = 0;

            for (int r = 0; r < N; ++r) {
                if (board[r][c] == 0) {
                    if (orientation == 2) {
                        ++cnt;
                    } else if (orientation == 3) {
                        tmp.push_front(0);
                    }
                } else {
                    tmp.push_back(board[r][c]);
                }
            }

            if (orientation == 2) {
                for (int i = 0; i < cnt; ++i) tmp.push_back(0);

                for (int i = 0; i < N - 1; ++i) {
                    if (tmp[i] != 0 && tmp[i] == tmp[i + 1]) {
                        tmp[i] *= 2;
                        tmp.erase(tmp.begin() + i + 1);
                        tmp.push_back(0);

                        if (tmp[i] > maxVal) maxVal = tmp[i];
                    }
                }
            } else if (orientation == 3) {
                for (int i = N - 1; i > 0; --i) {
                    if (tmp[i] != 0 && tmp[i] == tmp[i - 1]) {
                        tmp[i] *= 2;
                        tmp.erase(tmp.begin() + i - 1);
                        tmp.push_front(0);

                        if (tmp[i] > maxVal) maxVal = tmp[i];
                    }
                }
            }

            for (int i = 0; i < N; ++i) {
                board[i][c] = tmp[i];
            }
        }
    }
}

void playGame(int depth) {
    deque<int> nowBoard[20];

    if (depth > 5) return;

    for (int i = 0; i < N; ++i) {
        nowBoard[i] = board[i];
    }

    for (int i = 0; i < 4; ++i) {
        move(i);
        playGame(depth + 1);

        for (int i = 0; i < N; ++i) {
            board[i] = nowBoard[i];
        }
    }
}

int main() {
    scanf("%d", &N);

    for (int i = 0; i < N; ++i) {
        board[i].resize(N);
        for (int j = 0; j < N; ++j) {
            scanf("%d", &board[i][j]);

            if (board[i][j] > maxVal) maxVal = board[i][j];
        }
    }

    playGame(1);

    printf("%d", maxVal);

    return 0;
}