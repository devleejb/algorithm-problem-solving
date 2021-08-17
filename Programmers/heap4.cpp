#include <string>
#include <vector>
#include <algorithm>
#include <limits.h>

using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    vector<int> v;
    char op;
    string tmp = "";
    int num;
    int size = operations.size();

    for (int i = 0; i < size; i++)
    {
        op = operations[i].at(0); // 연산 종류
        tmp = "";

        for (int j = 2; j < operations[i].size(); j++)
        {
            tmp += operations[i].at(j);    
        }

        num = atoi(tmp.c_str());
        
        if (op == 'I')
        {
            v.push_back(num);
            push_heap(v.begin(), v.end());
        }
        else if (op == 'D')
        {
            if (!v.empty())
            {
                if (num == 1) // 가장 큰 수 삭제
                {
                    pop_heap(v.begin(), v.end());
                    v.pop_back();
                }
                else // 가장 작은 수 삭제
                {
                    int min = INT_MAX;
                    int min_idx;

                    for (int j = v.size() / 2; j < v.size(); j++) // 최솟값 찾기
                    {
                        if (v[j] < min)
                        {
                            min = v[j];
                            min_idx = j;
                        }
                    }

                    v.erase(v.begin() + min_idx);

                    make_heap(v.begin(), v.end());
                }
            }
        }
    }

    if (v.empty())
    {
        answer.push_back(0);
        answer.push_back(0);
    }
    else
    {
        int min = INT_MAX;
        
        answer.push_back(v[0]);
    
        for (int j = v.size() / 2; j < v.size(); j++) // 최솟값 찾기
        {
            if (v[j] < min)
            {
                min = v[j];
            }
        }

        answer.push_back(min);
    }
        
    return answer;
}