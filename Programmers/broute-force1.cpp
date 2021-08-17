#include <string>
#include <vector>

using namespace std;

// 찍는 방법 배열
int arr1[] = {1, 2, 3, 4, 5};
int arr2[] = {2, 1, 2, 3, 2, 4, 2, 5};
int arr3[] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
int score1, score2, score3;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    int size = answers.size();
    int ans;

    for (int i = 0; i < size; i++)
    {
        // 채점
        ans = answers[i];

        if (arr1[i % 5] == ans)
        {
            score1++;
        }

        if (arr2[i % 8] == ans)
        {
            score2++;
        }

        if (arr3[i % 10] == ans)
        {
            score3++;
        } 
    }
    
    // 최고점 계산
    ans = 0;

    if (score1 > ans)
    {
        ans = score1;
    }

    if (score2 > ans)
    {
        ans = score2;
    }

    if (score3 > ans)
    {
        ans = score3;
    }

    // answer vector 완성
    if (ans == score1)
    {
        answer.push_back(1);
    }

    if (ans == score2)
    {
        answer.push_back(2);
    }

    if (ans == score3)
    {
        answer.push_back(3);
    }

    return answer;
}
