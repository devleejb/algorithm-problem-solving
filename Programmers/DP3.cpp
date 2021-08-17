#include <string>
#include <vector>

using namespace std;

int ans[500][500];

int max(int a, int b) {
    if (a < b) return b;
    else return a;
}


int solution(vector<vector<int>> triangle) {
    int answer = 0;
    int size = triangle.size();

    ans[0][0] = triangle[0][0]; // 꼭짓점 초기화

    for (int i = 1; i < size; i++) // triangle 벡터 순회하며 최댓값 찾음
    {
        for (int j = 0; j <= i; j++)
        {
            if (j == 0)
            {
                ans[i][j] = ans[i - 1][0] + triangle[i][j];
            }
            else if (j == triangle[i].size())
            {
                ans[i][j] = ans[i - 1][j - 1] + triangle[i][j];
            }
            else
            {
                ans[i][j] = max(ans[i - 1][j - 1], ans[i - 1][j]) + triangle[i][j];
            }
        }   
    }

    for (int i = 0; i < size; i++)
    {
        if (ans[size - 1][i] > answer) // 최댓값 찾기
        {
            answer = ans[size - 1][i]; 
        }        
    }
    
    return answer;
}